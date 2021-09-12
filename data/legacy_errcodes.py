switch_known_errcode_ranges = {
    # NIM
    137: [
        [8001, 8096, 'libcurl error 1-96. Some of the libcurl errors in the error-table map to the above unknown-libcurl-error however.'],
    ],

    # FS
    2: [
        [2000, 2499, "Error: Failed to access SD card."],
        [2500, 2999, "Error: Failed to access game card. "],
        [3200, 3499, "nn::fs::ResultAllocationMemoryFailed: Error: Failed to allocate memory."],
        [3500, 3999, "Error: Failed to access MMC. "],
        [4001, 4299, "Error: ROM is corrupted. "],
        [4301, 4499, "Error: Save data is corrupted."],
        [4501, 4599, "Error: NCA is corrupted."],
        [4601, 4639, "Error: Integrity verification failed."],
        [4641, 4659, "Error: Partition FS is corrupted."],
        [4661, 4679, "Error: Built-in-storage is corrupted."],
        [4681, 4699, "Error: FAT FS is corrupted."],
        [4701, 4719, "Error: HOST FS is corrupted."],
        [4720, 4999, "nn::fs::ResultDataCorrupted: Error: Data is corrupted."],
        [5000, 5999, "Error: Unexpected failure occurred."],
        [6002, 6029, "Error: Invalid path was specified."],
        [6001, 6199, "Error: Invalid argument was specified."],
        [6202, 6299, "Error: Invalid operation for the open mode."],
        [6300, 6399, "Error: Unsupported operation."],
        [6400, 6499, "Error: Permission denied."],
    ],

    # NIFM Support Page Links
    110: [
        [2900, 2999, "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22277/p/897"],
        [2000, 2899, "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22263/p/897"],
    ]
}

special_err = {

    # Non-SwitchBrew Error Codes - Mostly stuff sent to me

    "0x7E12B": "Eshop connection failed",
    "0x39D689": "CDN Ban",
    "0x3E8E7C": "Error in account login/creation",
    "0x3E8EA0": "Failed connection test",
    "0x1F4E7C": "(normal) console ban",
    "0x27EE7C": "(potential) complete account ban",  # This error is still super new, needs more informations
    "0x36B72B": "Access token expired",
    "0x1F486E": "Internet connection lost because the console entered sleep mode.",
    "0x21C89": "Failed to base64-encode the EticketDeviceCertificate during an attempted AccountGetDynamicEtickets (personalized ticket) request to ecs.",
    "0x5089": "Failed to snprintf the AccountGetDynamicEtickets (personalized ticket) request JSON data.",
    "0x6410": "GetApplicationControlData: unable to find control for the input title ID",
    "0xa073": "NFC is disabled",
    "0x16473": "Could not mount tag (invalid tag type?)",
    "0x8073": "Device unavailable",
    "0x10073": "App area not found",
    "0x11073": "Tag corrupted?",
    "0xc880": "thrown by AM when qlaunch is terminated",
    "0xc87c": "invalid user",
    "0xc7e": "mii already exists",
    "0xa7e": "full database",
    "0x87e": "mii not found",
    "0x115b": "[HBL] Stopped loading NROs",
    "0x48c69": "device_cert_ecc_b223 failed to load",
    "0x138E02": "gamecard cmd buffer too small - must be '0x40 (or bigger)'",
    "0x138E02": "gc out of bounds sector access",
    "0x13DC02": "gc sector start is out of range for partition 1",
    "0x13D802": "gc sector end out of range for partition 1",
    "0x13DA02": "gc sector wrong partition access",
    

    # Libnx Errors from libnx/result.h

    # - Normal -
    "0x359": "LibnxError_BadReloc",
    "0x559": "LibnxError_OutOfMemory",
    "0x759": "LibnxError_AlreadyMapped",
    "0x959": "LibnxError_BadGetInfo_Stack",
    "0xB59": "LibnxError_BadGetInfo_Heap",
    "0xD59": "LibnxError_BadQueryMemory",
    "0xF59": "LibnxError_AlreadyInitialized",
    "0x1159": "LibnxError_NotInitialized",
    "0x1359": "LibnxError_NotFound",
    "0x1559": "LibnxError_IoError",
    "0x1759": "LibnxError_BadInput",
    "0x1959": "LibnxError_BadReent",
    "0x1B59": "LibnxError_BufferProducerError",
    "0x1D59": "LibnxError_HandleTooEarly",
    "0x1F59": "LibnxError_HeapAllocFailed",
    "0x2159": "LibnxError_TooManyOverrides",
    "0x2359": "LibnxError_ParcelError",
    "0x2559": "LibnxError_BadGfxInit",
    "0x2759": "LibnxError_BadGfxEventWait",
    "0x2959": "LibnxError_BadGfxQueueBuffer",
    "0x2B59": "LibnxError_BadGfxDequeueBuffer",
    "0x2D59": "LibnxError_AppletCmdidNotFound",
    "0x2F59": "LibnxError_BadAppletReceiveMessage",
    "0x3159": "LibnxError_BadAppletNotifyRunning",
    "0x3359": "LibnxError_BadAppletGetCurrentFocusState",
    "0x3559": "LibnxError_BadAppletGetOperationMode",
    "0x3759": "LibnxError_BadAppletGetPerformanceMode",
    "0x3959": "LibnxError_BadUsbCommsRead",
    "0x3B59": "LibnxError_BadUsbCommsWrite",
    "0x3D59": "LibnxError_InitFail_SM",
    "0x3F59": "LibnxError_InitFail_AM",
    "0x4159": "LibnxError_InitFail_HID",
    "0x4359": "LibnxError_InitFail_FS",
    "0x4559": "LibnxError_BadGetInfo_Rng",
    "0x4759": "LibnxError_JitUnavailable",
    "0x4959": "LibnxError_WeirdKernel",
    "0x4B59": "LibnxError_IncompatSysVer",
    "0x4D59": "LibnxError_InitFail_Time",
    "0x4F59": "LibnxError_TooManyDevOpTabs",
    "0x5159": "LibnxError_DomainMessageUnknownType",
    "0x5359": "LibnxError_DomainMessageTooManyObjectIds",
    "0x5559": "LibnxError_AppletFailedToInitialize",
    "0x5759": "LibnxError_ApmFailedToInitialize",
    "0x5959": "LibnxError_NvinfoFailedToInitialize",
    "0x5B59": "LibnxError_NvbufFailedToInitialize",
    "0x5D59": "LibnxError_LibAppletBadExit",

    # - Libnx Binder -
    "0x35D": "LibnxBinderError_Unknown",
    "0x55D": "LibnxBinderError_NoMemory",
    "0x75D": "LibnxBinderError_InvalidOperation",
    "0x95D": "LibnxBinderError_BadValue",
    "0xB5D": "LibnxBinderError_BadType",
    "0xD5D": "LibnxBinderError_NameNotFound",
    "0xF5D": "LibnxBinderError_PermissionDenied",
    "0x115D": "LibnxBinderError_NoInit",
    "0x135D": "LibnxBinderError_AlreadyExists",
    "0x155D": "LibnxBinderError_DeadObject",
    "0x175D": "LibnxBinderError_FailedTransaction",
    "0x195D": "LibnxBinderError_BadIndex",
    "0x1B5D": "LibnxBinderError_NotEnoughData",
    "0x1D5D": "LibnxBinderError_WouldBlock",
    "0x1F5D": "LibnxBinderError_TimedOut",
    "0x215D": "LibnxBinderError_UnknownTransaction",
    "0x235D": "LibnxBinderError_FdsNotAllowed",

    # - LibNX Nvidia -
    "0x35C": "LibnxNvidiaError_Unknown",
    "0x55C": "LibnxNvidiaError_NotImplemented",
    "0x75C": "LibnxNvidiaError_NotSupported",
    "0x95C": "LibnxNvidiaError_NotInitialized",
    "0xB5C": "LibnxNvidiaError_BadParameter",
    "0xD5C": "LibnxNvidiaError_Timeout",
    "0xF5C": "LibnxNvidiaError_InsufficientMemory",
    "0x115C": "LibnxNvidiaError_ReadOnlyAttribute",
    "0x135C": "LibnxNvidiaError_InvalidState",
    "0x155C": "LibnxNvidiaError_InvalidAddress",
    "0x175C": "LibnxNvidiaError_InvalidSize",
    "0x195C": "LibnxNvidiaError_BadValue",
    "0x1B5C": "LibnxNvidiaError_AlreadyAllocated",
    "0x1D5C": "LibnxNvidiaError_Busy",
    "0x1F5C": "LibnxNvidiaError_ResourceError",
    "0x215C": "LibnxNvidiaError_CountMismatch",
    "0x235C": "LibnxNvidiaError_SharedMemoryTooSmall",
    "0x255C": "LibnxNvidiaError_FileOperationFailed",
    "0x275C": "LibnxNvidiaError_IoctlFailed",

    # "0x3E8E89: 'Failed to access Firmware Updates - Often because of DNS!',
    # ^ Also used by libcurl

    # Atmosphere

    "0xCAFEF": "Atmosphere: Version Mismatch",

    # Pegaswitch

    "0xa7200": "Fake-Error by Pegaswitch",

    # Old Atmos
    
    "0x0": "If this happens, you\'re on an very old version of Atmosphere. Please update Atmosphere/Kosmos to fix this.",

    # Funny MaiMai
    
    "0xdeadbeef": "E A S T E R  E G G",

    # https://github.com/tumGER/BETCH/issues/18
    
    "0x3ed32": "Error caused by failure to connect to a working server.",

    # https://github.com/tumGER/BETCH/issues/25
    
    "0x8a2": "Atmosphere: ForcedShutdownDetected",

    }

# Game Erros - Strings because Nintendo decided that it would be useless to put them into normal ints ;^)
# Attention: These need to be formatted -> <errcode>: "<game>: <description>" - Also Nintendo support codes
switch_game_err = {
    # Splatoon 2
    "2-AAB6A-3400": "Splatoon 2: A kick from online due to exefs edits.",

    # Youtube
    "2-ARVHA-0000": "Youtube: Unknown Error",
}

switch_support_page = {
    # Nintendo Support Page
    "2005-0003": "This error code may indicate an issue related to the microSD card being used. (https://en-americas-support.nintendo.com/app/answers/detail/a_id/22393/p/897)",
    "2110-1100": "This error code typically indicates that the Nintendo Switch console was unable to detect a network which matches any of the saved networks within the Internet settings. (https://en-americas-support.nintendo.com/app/answers/detail/a_id/22780/p/897)",
    "2618-0516": "This error code generally indicates that your network is not optimal for peer to peer connections, likely due to your network's NAT type. (https://en-americas-support.nintendo.com/app/answers/detail/a_id/25855/p/897)",
    "2110-2003": "Error codes in this range generally indicate an error occurred when the Nintendo Switch console attempted to initially connect to a wireless router (usually prior to obtaining an IP address). (https://en-americas-support.nintendo.com/app/answers/detail/a_id/27023/p/897)",
    "2813-6838": "You are unable to redeem a Nintendo eShop Card (https://en-americas-support.nintendo.com/app/answers/detail/a_id/22630/p/897)",
    "2813-6561": "In most cases, this error indicates the Nintendo eShop card or download code was entered incorrectly, or was intended for a different region's Nintendo eShop. (https://en-americas-support.nintendo.com/app/answers/detail/a_id/25870/p/897)",
    "2618-0513": "This error code generally indicates that your network is not optimal for peer to peer connections, this may be due to the ISP, Internet connection speeds, or due to your network's NAT type. (https://en-americas-support.nintendo.com/app/answers/detail/a_id/25980/p/897)",
    "2618-0201": "This error may be the result your connection timing out due to a slow Internet service or a poor wireless environment. (https://en-americas-support.nintendo.com/app/answers/detail/a_id/25866/p/897)",
    "2002-0001": "An error code is received when powering up the Nintendo Switch console, or when coming out of sleep mode. (https://en-americas-support.nintendo.com/app/answers/detail/a_id/27167/p/897)",
    "2813-1470": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/26362/p/897",
    "2124-4007": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/28046/p/897",
    "2811-5001": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22392/p/897",
    "2110-3127": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22567/p/897",
    "9001-0026": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/27311/p/897",
    "2124-8006": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/25858/p/897",
    "2124-8007": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/25858/p/897",
    "2137-8006": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22493/p/897",
    "2155-8007": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/42264/p/897",
    "2811-1006": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/25859/p/897",
    "2813-0055": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/27056/p/897",
    "2181-4008": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/42061/p/897",
    "2137-8056": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/28910/p/897",
    "2618-0502": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/25865/p/897",
    "2618-0501": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/25865/p/897",
    "2162-0002": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22596/p/897",
    "2137-8035": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22298/p/897",
    "2618-0006": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/25856/p/897",
    "2016-0641": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/27004/p/897",
    "2016-0247": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22720/p/897",
    "2124-8028": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22443/p/897",
    "2811-1028": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22503/p/897",
    "2306-0303": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/42878/p/897",
    "2123-0301": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/28291/p/897",
    "2168-0002": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22518/p/897",
    "2160-8007": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/28530/p/897",
    "2160-8006": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/28530/p/897",
    "2101-0001": "https://en-americas-support.nintendo.com/app/answers/detail/a_id/22624/p/897",
    # If somebody wants to continue this: https://en-americas-support.nintendo.com/app/answers/list/st/5/kw/error%20code/p/897/page/5
}