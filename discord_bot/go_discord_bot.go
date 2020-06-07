package main

import (
	"fmt"
	"regexp"
	//"net/http"
	"os"
	"os/signal"
	"strconv"
	"strings"
	"syscall"

	"github.com/Lukaesebrot/dgc"
	"github.com/bwmarrin/discordgo"
)

func main() {
	bot, err := discordgo.New("Bot " + "Token")
	if err != nil {
		fmt.Println("Error authenticating to discord: ", err)
		return
	}

	err = bot.Open()
	if err != nil {
		fmt.Println("Error opening connection to discord", err)
		return
	}

	fmt.Println("Logged into Discord successfully")

	// Wait till we die, like in reality
	defer func() {
		sc := make(chan os.Signal, 1)
		signal.Notify(sc, syscall.SIGINT, syscall.SIGTERM, os.Interrupt, os.Kill)
		<-sc

		bot.Close()
		fmt.Println("Closed connection to Discord. Goodbye.")
	}()

	// Create a dgc router
	router := dgc.Create(&dgc.Router{
		Prefixes:    []string{"."},
		BotsAllowed: false,
	},
	)

	router.RegisterDefaultHelpCommand(bot, nil) // Add help command

	router.RegisterCmd(&dgc.Command{
		Name: "err",
		Aliases: []string{
			"serr",
			"error",
			"nxerr",
		},
		Description: "Shows relevant details for your error code",
		Usage:       ".serr <ERROR CODE>",
		Example:     ".serr 2000-0000",
		IgnoreCase:  true,
		Handler:     errSearcher,
	})

	router.RegisterCmd(&dgc.Command{
		Name:        "module",
		Description: "Shows relevant details about the module",
		Usage:       ".module <ERROR CODE>",
		Example:     ".module 2000-0000",
		IgnoreCase:  true,
		Handler:     moduleSearcher,
	})

	router.Initialize(bot)
}

func errSearcher(ctx *dgc.Ctx) {

	var re = regexp.MustCompile(`(?m)2\d{3}\-\d{4}`)

	// Searches for error codes in the database
	if ctx.Arguments.Amount() != 1 {
		ctx.RespondText("Please only send a single error code!")
		return
	}

	arg := ctx.Arguments.Raw()
	
	if re.MatchString(arg) {
		arrErrParts := strings.SplitN(arg, "-", 2)
		module := arrErrParts[0]
		desc := arrErrParts[1]
		descInt, err := strconv.Atoi((desc))
		if err != nil {}
		moduleInt, err := strconv.Atoi(module)
		if err != nil {}
		moduleInt -= 2000

		errcode := (descInt << 9) + moduleInt

		ctx.RespondText(string(arg))
		ctx.RespondText(fmt.Sprintf("The following error code was given to me as a string: %#x", errcode))

	} else if strings.HasPrefix(arg, "0x") {
		errcode, err := strconv.ParseInt(arg, 0, 0)
		if err != nil {
			ctx.RespondText("Error converting hex")
			fmt.Println(err)
			return
		}
		module := errcode & 0x1FF
		desc := (errcode >> 9) & 0x3FFF
		decErr := fmt.Sprint(module + 2000, "-", desc)

		ctx.RespondText(string(decErr))
		ctx.RespondText("The following error code was given to me in hex: " + arg)
	}
}

func moduleSearcher(ctx *dgc.Ctx) {
	// Searches for modules and infos related to them inside the database
	if ctx.Arguments.Amount() != 1 {
		ctx.RespondText("Too many arguments!")
		return
	}

	// resp, err := http.Get("http://err.tomger.eu/api/betch/all")
	//if err != nil {
	//	ctx.RespondText("BETCH API seems to be unavailable!")
	//	return
	//}

	// module := ctx.Arguments.Raw()
}
