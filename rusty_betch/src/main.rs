// Example for the following slash command structure:
// {
//     "name": "foo",
//     "description": "hello",
//     "options": [
//         {
//             "type": 3,
//             "name": "text",
//             "description": "aaa",
//             "required": true
//         },
//         {
//             "type": 7,
//             "name": "channel",
//             "description": "bbb",
//             "required": true
//         },
//         {
//             "type": 4,
//             "name": "integer",
//             "description": "ccc",
//             "required": false
//         }
//     ]
// }
//
// Additionally, set the DISCORD_TOKEN and DISCORD_ID environment variables

use serenity::client::{Context, EventHandler};
use serenity::model::interactions::application_command::ApplicationCommandInteraction;
use serenity::model::interactions::{Interaction, InteractionResponseType};
use serenity::{async_trait, Client};
use serenity_slash_decode::Error as SlashError;
use serenity_slash_decode::{process, SlashMap};
use std::fmt::{Display, Formatter};
use std::str::FromStr;
use dotenv::dotenv;
enum CustomError {
    SlashError(SlashError),
    CommandNotFound(String),
}

impl Display for CustomError {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        match self {
            // serenity-slash-decode's error type implements Display
            CustomError::SlashError(e) => e.fmt(f),
            CustomError::CommandNotFound(s) => f.write_str(&*format!("Command `{}` not found", s)),
        }
    }
}

impl From<SlashError> for CustomError {
    fn from(e: SlashError) -> Self {
        CustomError::SlashError(e)
    }
}

type CustomResult<T> = Result<T, CustomError>;

async fn handle_command(
    ctx: &Context,
    interaction: &ApplicationCommandInteraction,
    args: SlashMap,
) -> CustomResult<()> {
    let mut message = format!(
        "text: {}\nchannel: {}",
        args.get_string("text")?,
        args.get_channel("channel")?.name
    );
    match args.get_integer("integer") {
        Ok(s) => message.push_str(&*format!("\ninteger: {}", s)),
        Err(_) => {}
    };
    interaction
        .create_interaction_response(ctx.http.clone(), |response| {
            response
                .kind(InteractionResponseType::ChannelMessageWithSource)
                .interaction_response_data(|data| data.content(message))
        })
        .await;
    Ok(())
}

struct Handler;

#[async_trait]
impl EventHandler for Handler {
    async fn interaction_create(&self, ctx: Context, interaction: Interaction) {
        // only handle slash commands
        let data = match &interaction {
            Interaction::ApplicationCommand(s) => &s.data,
            _ => return,
        };
        let (path, args) = process(&data);
        let command = interaction.application_command().unwrap();
        match match path.as_str() {
            "foo" => handle_command(&ctx, &command, args).await,
            _ => Err(CustomError::CommandNotFound(path)),
        } {
            Ok(_) => {}
            Err(e) => {
                command
                    .create_interaction_response(ctx.http, |response| {
                        response
                            .kind(InteractionResponseType::ChannelMessageWithSource)
                            .interaction_response_data(|data| data.content(format!("Error: {}", e)))
                    })
                    .await;
            }
        };
    }
}

#[tokio::main]
async fn main() {
    dotenv().expect("F, file missing and shit");

    // make sure to set these environment variables!
    let mut client = Client::builder(std::env::var("DISCORD_TOKEN").unwrap())
        .application_id(u64::from_str(&*std::env::var("DISCORD_ID").unwrap()).unwrap())
        .event_handler(Handler)
        .await
        .unwrap();
    if let Err(e) = client.start().await {
        println!("Runtime error: {:?}", e);
    }
}