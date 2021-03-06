
complete --command youtube-dl --long-option help --short-option h --description 'Print this help text and exit'
complete --command youtube-dl --long-option version --description 'Print program version and exit'
complete --command youtube-dl --long-option update --short-option U --description 'Update this program to latest version. Make sure that you have sufficient permissions (run with sudo if needed)'
complete --command youtube-dl --long-option ignore-errors --short-option i --description 'Continue on download errors, for example to skip unavailable videos in a playlist'
complete --command youtube-dl --long-option abort-on-error --description 'Abort downloading of further videos (in the playlist or the command line) if an error occurs'
complete --command youtube-dl --long-option dump-user-agent --description 'Display the current browser identification'
complete --command youtube-dl --long-option list-extractors --description 'List all supported extractors'
complete --command youtube-dl --long-option extractor-descriptions --description 'Output descriptions of all supported extractors'
complete --command youtube-dl --long-option force-generic-extractor --description 'Force extraction to use the generic extractor'
complete --command youtube-dl --long-option default-search --description 'Use this prefix for unqualified URLs. For example "gvsearch2:" downloads two videos from google videos for youtube-dl "large apple". Use the value "auto" to let youtube-dl guess ("auto_warning" to emit a warning when guessing). "error" just throws an error. The default value "fixup_error" repairs broken URLs, but emits an error if this is not possible instead of searching.'
complete --command youtube-dl --long-option ignore-config --description 'Do not read configuration files. When given in the global configuration file /etc/youtube-dl.conf: Do not read the user configuration in ~/.config/youtube-dl/config (%APPDATA%/youtube-dl/config.txt on Windows)'
complete --command youtube-dl --long-option config-location --description 'Location of the configuration file; either the path to the config or its containing directory.'
complete --command youtube-dl --long-option flat-playlist --description 'Do not extract the videos of a playlist, only list them.'
complete --command youtube-dl --long-option mark-watched --description 'Mark videos watched (YouTube only)'
complete --command youtube-dl --long-option no-mark-watched --description 'Do not mark videos watched (YouTube only)'
complete --command youtube-dl --long-option no-color --description 'Do not emit color codes in output'
complete --command youtube-dl --long-option proxy --description 'Use the specified HTTP/HTTPS/SOCKS proxy. To enable SOCKS proxy, specify a proper scheme. For example socks5://127.0.0.1:1080/. Pass in an empty string (--proxy "") for direct connection'
complete --command youtube-dl --long-option socket-timeout --description 'Time to wait before giving up, in seconds'
complete --command youtube-dl --long-option source-address --description 'Client-side IP address to bind to'
complete --command youtube-dl --long-option force-ipv4 --short-option 4 --description 'Make all connections via IPv4'
complete --command youtube-dl --long-option force-ipv6 --short-option 6 --description 'Make all connections via IPv6'
complete --command youtube-dl --long-option geo-verification-proxy --description 'Use this proxy to verify the IP address for some geo-restricted sites. The default proxy specified by --proxy (or none, if the option is not present) is used for the actual downloading.'
complete --command youtube-dl --long-option cn-verification-proxy
complete --command youtube-dl --long-option geo-bypass --description 'Bypass geographic restriction via faking X-Forwarded-For HTTP header'
complete --command youtube-dl --long-option no-geo-bypass --description 'Do not bypass geographic restriction via faking X-Forwarded-For HTTP header'
complete --command youtube-dl --long-option geo-bypass-country --description 'Force bypass geographic restriction with explicitly provided two-letter ISO 3166-2 country code'
complete --command youtube-dl --long-option geo-bypass-ip-block --description 'Force bypass geographic restriction with explicitly provided IP block in CIDR notation'
complete --command youtube-dl --long-option playlist-start --description 'Playlist video to start at (default is %default)'
complete --command youtube-dl --long-option playlist-end --description 'Playlist video to end at (default is last)'
complete --command youtube-dl --long-option playlist-items --description 'Playlist video items to download. Specify indices of the videos in the playlist separated by commas like: "--playlist-items 1,2,5,8" if you want to download videos indexed 1, 2, 5, 8 in the playlist. You can specify range: "--playlist-items 1-3,7,10-13", it will download the videos at index 1, 2, 3, 7, 10, 11, 12 and 13.'
complete --command youtube-dl --long-option match-title --description 'Download only matching titles (regex or caseless sub-string)'
complete --command youtube-dl --long-option reject-title --description 'Skip download for matching titles (regex or caseless sub-string)'
complete --command youtube-dl --long-option max-downloads --description 'Abort after downloading NUMBER files'
complete --command youtube-dl --long-option min-filesize --description 'Do not download any videos smaller than SIZE (e.g. 50k or 44.6m)'
complete --command youtube-dl --long-option max-filesize --description 'Do not download any videos larger than SIZE (e.g. 50k or 44.6m)'
complete --command youtube-dl --long-option date --description 'Download only videos uploaded in this date'
complete --command youtube-dl --long-option datebefore --description 'Download only videos uploaded on or before this date (i.e. inclusive)'
complete --command youtube-dl --long-option dateafter --description 'Download only videos uploaded on or after this date (i.e. inclusive)'
complete --command youtube-dl --long-option min-views --description 'Do not download any videos with less than COUNT views'
complete --command youtube-dl --long-option max-views --description 'Do not download any videos with more than COUNT views'
complete --command youtube-dl --long-option match-filter --description 'Generic video filter. Specify any key (see the "OUTPUT TEMPLATE" for a list of available keys) to match if the key is present, !key to check if the key is not present, key > NUMBER (like "comment_count > 12", also works with >=, <, <=, !=, =) to compare against a number, key = '"'"'LITERAL'"'"' (like "uploader = '"'"'Mike Smith'"'"'", also works with !=) to match against a string literal and & to require multiple matches. Values which are not known are excluded unless you put a question mark (?) after the operator. For example, to only match videos that have been liked more than 100 times and disliked less than 50 times (or the dislike functionality is not available at the given service), but who also have a description, use --match-filter "like_count > 100 & dislike_count <? 50 & description" .'
complete --command youtube-dl --long-option no-playlist --description 'Download only the video, if the URL refers to a video and a playlist.'
complete --command youtube-dl --long-option yes-playlist --description 'Download the playlist, if the URL refers to a video and a playlist.'
complete --command youtube-dl --long-option age-limit --description 'Download only videos suitable for the given age'
complete --command youtube-dl --long-option download-archive --description 'Download only videos not listed in the archive file. Record the IDs of all downloaded videos in it.' --require-parameter
complete --command youtube-dl --long-option include-ads --description 'Download advertisements as well (experimental)'
complete --command youtube-dl --long-option limit-rate --short-option r --description 'Maximum download rate in bytes per second (e.g. 50K or 4.2M)'
complete --command youtube-dl --long-option retries --short-option R --description 'Number of retries (default is %default), or "infinite".'
complete --command youtube-dl --long-option fragment-retries --description 'Number of retries for a fragment (default is %default), or "infinite" (DASH, hlsnative and ISM)'
complete --command youtube-dl --long-option skip-unavailable-fragments --description 'Skip unavailable fragments (DASH, hlsnative and ISM)'
complete --command youtube-dl --long-option abort-on-unavailable-fragment --description 'Abort downloading when some fragment is not available'
complete --command youtube-dl --long-option keep-fragments --description 'Keep downloaded fragments on disk after downloading is finished; fragments are erased by default'
complete --command youtube-dl --long-option buffer-size --description 'Size of download buffer (e.g. 1024 or 16K) (default is %default)'
complete --command youtube-dl --long-option no-resize-buffer --description 'Do not automatically adjust the buffer size. By default, the buffer size is automatically resized from an initial value of SIZE.'
complete --command youtube-dl --long-option http-chunk-size --description 'Size of a chunk for chunk-based HTTP downloading (e.g. 10485760 or 10M) (default is disabled). May be useful for bypassing bandwidth throttling imposed by a webserver (experimental)'
complete --command youtube-dl --long-option test
complete --command youtube-dl --long-option playlist-reverse --description 'Download playlist videos in reverse order'
complete --command youtube-dl --long-option playlist-random --description 'Download playlist videos in random order'
complete --command youtube-dl --long-option xattr-set-filesize --description 'Set file xattribute ytdl.filesize with expected file size'
complete --command youtube-dl --long-option hls-prefer-native --description 'Use the native HLS downloader instead of ffmpeg'
complete --command youtube-dl --long-option hls-prefer-ffmpeg --description 'Use ffmpeg instead of the native HLS downloader'
complete --command youtube-dl --long-option hls-use-mpegts --description 'Use the mpegts container for HLS videos, allowing to play the video while downloading (some players may not be able to play it)'
complete --command youtube-dl --long-option external-downloader --description 'Use the specified external downloader. Currently supports aria2c,avconv,axel,curl,ffmpeg,httpie,wget'
complete --command youtube-dl --long-option external-downloader-args --description 'Give these arguments to the external downloader'
complete --command youtube-dl --long-option batch-file --short-option a --description 'File containing URLs to download ('"'"'-'"'"' for stdin), one URL per line. Lines starting with '"'"'#'"'"', '"'"';'"'"' or '"'"']'"'"' are considered as comments and ignored.' --require-parameter
complete --command youtube-dl --long-option id --description 'Use only video ID in file name'
complete --command youtube-dl --long-option output --short-option o --description 'Output filename template, see the "OUTPUT TEMPLATE" for all the info'
complete --command youtube-dl --long-option autonumber-size
complete --command youtube-dl --long-option autonumber-start --description 'Specify the start value for %(autonumber)s (default is %default)'
complete --command youtube-dl --long-option restrict-filenames --description 'Restrict filenames to only ASCII characters, and avoid "&" and spaces in filenames'
complete --command youtube-dl --long-option auto-number --short-option A
complete --command youtube-dl --long-option title --short-option t
complete --command youtube-dl --long-option literal --short-option l
complete --command youtube-dl --long-option no-overwrites --short-option w --description 'Do not overwrite files'
complete --command youtube-dl --long-option continue --short-option c --description 'Force resume of partially downloaded files. By default, youtube-dl will resume downloads if possible.'
complete --command youtube-dl --long-option no-continue --description 'Do not resume partially downloaded files (restart from beginning)'
complete --command youtube-dl --long-option no-part --description 'Do not use .part files - write directly into output file'
complete --command youtube-dl --long-option no-mtime --description 'Do not use the Last-modified header to set the file modification time'
complete --command youtube-dl --long-option write-description --description 'Write video description to a .description file'
complete --command youtube-dl --long-option write-info-json --description 'Write video metadata to a .info.json file'
complete --command youtube-dl --long-option write-annotations --description 'Write video annotations to a .annotations.xml file'
complete --command youtube-dl --long-option load-info-json --description 'JSON file containing the video information (created with the "--write-info-json" option)'
complete --command youtube-dl --long-option cookies --description 'File to read cookies from and dump cookie jar in' --require-parameter
complete --command youtube-dl --long-option cache-dir --description 'Location in the filesystem where youtube-dl can store some downloaded information permanently. By default $XDG_CACHE_HOME/youtube-dl or ~/.cache/youtube-dl . At the moment, only YouTube player files (for videos with obfuscated signatures) are cached, but that may change.'
complete --command youtube-dl --long-option no-cache-dir --description 'Disable filesystem caching'
complete --command youtube-dl --long-option rm-cache-dir --description 'Delete all filesystem cache files'
complete --command youtube-dl --long-option write-thumbnail --description 'Write thumbnail image to disk'
complete --command youtube-dl --long-option write-all-thumbnails --description 'Write all thumbnail image formats to disk'
complete --command youtube-dl --long-option list-thumbnails --description 'Simulate and list all available thumbnail formats'
complete --command youtube-dl --long-option quiet --short-option q --description 'Activate quiet mode'
complete --command youtube-dl --long-option no-warnings --description 'Ignore warnings'
complete --command youtube-dl --long-option simulate --short-option s --description 'Do not download the video and do not write anything to disk'
complete --command youtube-dl --long-option skip-download --description 'Do not download the video'
complete --command youtube-dl --long-option get-url --short-option g --description 'Simulate, quiet but print URL'
complete --command youtube-dl --long-option get-title --short-option e --description 'Simulate, quiet but print title'
complete --command youtube-dl --long-option get-id --description 'Simulate, quiet but print id'
complete --command youtube-dl --long-option get-thumbnail --description 'Simulate, quiet but print thumbnail URL'
complete --command youtube-dl --long-option get-description --description 'Simulate, quiet but print video description'
complete --command youtube-dl --long-option get-duration --description 'Simulate, quiet but print video length'
complete --command youtube-dl --long-option get-filename --description 'Simulate, quiet but print output filename'
complete --command youtube-dl --long-option get-format --description 'Simulate, quiet but print output format'
complete --command youtube-dl --long-option dump-json --short-option j --description 'Simulate, quiet but print JSON information. See the "OUTPUT TEMPLATE" for a description of available keys.'
complete --command youtube-dl --long-option dump-single-json --short-option J --description 'Simulate, quiet but print JSON information for each command-line argument. If the URL refers to a playlist, dump the whole playlist information in a single line.'
complete --command youtube-dl --long-option print-json --description 'Be quiet and print the video information as JSON (video is still being downloaded).'
complete --command youtube-dl --long-option newline --description 'Output progress bar as new lines'
complete --command youtube-dl --long-option no-progress --description 'Do not print progress bar'
complete --command youtube-dl --long-option console-title --description 'Display progress in console titlebar'
complete --command youtube-dl --long-option verbose --short-option v --description 'Print various debugging information'
complete --command youtube-dl --long-option dump-pages --description 'Print downloaded pages encoded using base64 to debug problems (very verbose)'
complete --command youtube-dl --long-option write-pages --description 'Write downloaded intermediary pages to files in the current directory to debug problems'
complete --command youtube-dl --long-option youtube-print-sig-code
complete --command youtube-dl --long-option print-traffic --description 'Display sent and read HTTP traffic'
complete --command youtube-dl --long-option call-home --short-option C --description 'Contact the youtube-dl server for debugging'
complete --command youtube-dl --long-option no-call-home --description 'Do NOT contact the youtube-dl server for debugging'
complete --command youtube-dl --long-option encoding --description 'Force the specified encoding (experimental)'
complete --command youtube-dl --long-option no-check-certificate --description 'Suppress HTTPS certificate validation'
complete --command youtube-dl --long-option prefer-insecure --description 'Use an unencrypted connection to retrieve information about the video. (Currently supported only for YouTube)'
complete --command youtube-dl --long-option user-agent --description 'Specify a custom user agent'
complete --command youtube-dl --long-option referer --description 'Specify a custom referer, use if the video access is restricted to one domain'
complete --command youtube-dl --long-option add-header --description 'Specify a custom HTTP header and its value, separated by a colon '"'"':'"'"'. You can use this option multiple times'
complete --command youtube-dl --long-option bidi-workaround --description 'Work around terminals that lack bidirectional text support. Requires bidiv or fribidi executable in PATH'
complete --command youtube-dl --long-option sleep-interval --description 'Number of seconds to sleep before each download when used alone or a lower bound of a range for randomized sleep before each download (minimum possible number of seconds to sleep) when used along with --max-sleep-interval.'
complete --command youtube-dl --long-option max-sleep-interval --description 'Upper bound of a range for randomized sleep before each download (maximum possible number of seconds to sleep). Must only be used along with --min-sleep-interval.'
complete --command youtube-dl --long-option format --short-option f --description 'Video format code, see the "FORMAT SELECTION" for all the info'
complete --command youtube-dl --long-option all-formats --description 'Download all available video formats'
complete --command youtube-dl --long-option prefer-free-formats --description 'Prefer free video formats unless a specific one is requested'
complete --command youtube-dl --long-option list-formats --short-option F --description 'List all available formats of requested videos'
complete --command youtube-dl --long-option youtube-include-dash-manifest
complete --command youtube-dl --long-option youtube-skip-dash-manifest --description 'Do not download the DASH manifests and related data on YouTube videos'
complete --command youtube-dl --long-option merge-output-format --description 'If a merge is required (e.g. bestvideo+bestaudio), output to given container format. One of mkv, mp4, ogg, webm, flv. Ignored if no merge is required'
complete --command youtube-dl --long-option write-sub --description 'Write subtitle file'
complete --command youtube-dl --long-option write-auto-sub --description 'Write automatically generated subtitle file (YouTube only)'
complete --command youtube-dl --long-option all-subs --description 'Download all the available subtitles of the video'
complete --command youtube-dl --long-option list-subs --description 'List all available subtitles for the video'
complete --command youtube-dl --long-option sub-format --description 'Subtitle format, accepts formats preference, for example: "srt" or "ass/srt/best"'
complete --command youtube-dl --long-option sub-lang --description 'Languages of the subtitles to download (optional) separated by commas, use --list-subs for available language tags'
complete --command youtube-dl --long-option username --short-option u --description 'Login with this account ID'
complete --command youtube-dl --long-option password --short-option p --description 'Account password. If this option is left out, youtube-dl will ask interactively.'
complete --command youtube-dl --long-option twofactor --short-option 2 --description 'Two-factor authentication code'
complete --command youtube-dl --long-option netrc --short-option n --description 'Use .netrc authentication data'
complete --command youtube-dl --long-option video-password --description 'Video password (vimeo, smotri, youku)'
complete --command youtube-dl --long-option ap-mso --description 'Adobe Pass multiple-system operator (TV provider) identifier, use --ap-list-mso for a list of available MSOs'
complete --command youtube-dl --long-option ap-username --description 'Multiple-system operator account login'
complete --command youtube-dl --long-option ap-password --description 'Multiple-system operator account password. If this option is left out, youtube-dl will ask interactively.'
complete --command youtube-dl --long-option ap-list-mso --description 'List all supported multiple-system operators'
complete --command youtube-dl --long-option extract-audio --short-option x --description 'Convert video files to audio-only files (requires ffmpeg or avconv and ffprobe or avprobe)'
complete --command youtube-dl --long-option audio-format --description 'Specify audio format: "best", "aac", "flac", "mp3", "m4a", "opus", "vorbis", or "wav"; "%default" by default; No effect without -x'
complete --command youtube-dl --long-option audio-quality --description 'Specify ffmpeg/avconv audio quality, insert a value between 0 (better) and 9 (worse) for VBR or a specific bitrate like 128K (default %default)'
complete --command youtube-dl --long-option recode-video --description 'Encode the video to another format if necessary (currently supported: mp4|flv|ogg|webm|mkv|avi)' --arguments 'mp4 flv ogg webm mkv' --exclusive
complete --command youtube-dl --long-option postprocessor-args --description 'Give these arguments to the postprocessor'
complete --command youtube-dl --long-option keep-video --short-option k --description 'Keep the video file on disk after the post-processing; the video is erased by default'
complete --command youtube-dl --long-option no-post-overwrites --description 'Do not overwrite post-processed files; the post-processed files are overwritten by default'
complete --command youtube-dl --long-option embed-subs --description 'Embed subtitles in the video (only for mp4, webm and mkv videos)'
complete --command youtube-dl --long-option embed-thumbnail --description 'Embed thumbnail in the audio as cover art'
complete --command youtube-dl --long-option add-metadata --description 'Write metadata to the video file'
complete --command youtube-dl --long-option metadata-from-title --description 'Parse additional metadata like song title / artist from the video title. The format syntax is the same as --output. Regular expression with named capture groups may also be used. The parsed parameters replace existing values. Example: --metadata-from-title "%(artist)s - %(title)s" matches a title like "Coldplay - Paradise". Example (regex): --metadata-from-title "(?P<artist>.+?) - (?P<title>.+)"'
complete --command youtube-dl --long-option xattrs --description 'Write metadata to the video file'"'"'s xattrs (using dublin core and xdg standards)'
complete --command youtube-dl --long-option fixup --description 'Automatically correct known faults of the file. One of never (do nothing), warn (only emit a warning), detect_or_warn (the default; fix file if we can, warn otherwise)'
complete --command youtube-dl --long-option prefer-avconv --description 'Prefer avconv over ffmpeg for running the postprocessors'
complete --command youtube-dl --long-option prefer-ffmpeg --description 'Prefer ffmpeg over avconv for running the postprocessors (default)'
complete --command youtube-dl --long-option ffmpeg-location --description 'Location of the ffmpeg/avconv binary; either the path to the binary or its containing directory.'
complete --command youtube-dl --long-option exec --description 'Execute a command on the file after downloading, similar to find'"'"'s -exec syntax. Example: --exec '"'"'adb push {} /sdcard/Music/ && rm {}'"'"''
complete --command youtube-dl --long-option convert-subs --description 'Convert the subtitles to other format (currently supported: srt|ass|vtt|lrc)'


complete --command youtube-dl --arguments ":ytfavorites :ytrecommended :ytsubscriptions :ytwatchlater :ythistory"
