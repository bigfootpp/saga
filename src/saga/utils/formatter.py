LANGUAGE_TO_FLAG: dict[str, str] = {
    "fr": "🇫🇷",
    "fra": "🇫🇷",
    "fre": "🇫🇷",
    "en": "🇬🇧",
    "eng": "🇬🇧",
    "dual": "🇬🇧",
    "ja": "🇯🇵",
    "jpn": "🇯🇵",
    "jap": "🇯🇵",
    "de": "🇩🇪",
    "deu": "🇩🇪",
    "ger": "🇩🇪",
    "es": "🇪🇸",
    "spa": "🇪🇸",
    "lat": "🇲🇽",
    "it": "🇮🇹",
    "ita": "🇮🇹",
    "pt": "🇵🇹",
    "por": "🇵🇹",
    "pt-br": "🇧🇷",
    "ru": "🇷🇺",
    "rus": "🇷🇺",
    "uk": "🇺🇦",
    "ukr": "🇺🇦",
    "ko": "🇰🇷",
    "kor": "🇰🇷",
    "zh": "🇨🇳",
    "chi": "🇨🇳",
    "zho": "🇨🇳",
    "cmn": "🇨🇳",
    "hi": "🇮🇳",
    "hin": "🇮🇳",
    "nl": "🇳🇱",
    "nld": "🇳🇱",
    "dut": "🇳🇱",
    "pl": "🇵🇱",
    "pol": "🇵🇱",
    "cs": "🇨🇿",
    "cze": "🇨🇿",
    "ces": "🇨🇿",
    "sk": "🇸🇰",
    "slk": "🇸🇰",
    "slo": "🇸🇰",
    "hu": "🇭🇺",
    "hun": "🇭🇺",
    "ro": "🇷🇴",
    "ron": "🇷🇴",
    "rum": "🇷🇴",
    "bg": "🇧🇬",
    "bul": "🇧🇬",
    "el": "🇬🇷",
    "ell": "🇬🇷",
    "gre": "🇬🇷",
    "sv": "🇸🇪",
    "swe": "🇸🇪",
    "da": "🇩🇰",
    "dan": "🇩🇰",
    "no": "🇳🇴",
    "nor": "🇳🇴",
    "fi": "🇫🇮",
    "fin": "🇫🇮",
    "tr": "🇹🇷",
    "tur": "🇹🇷",
    "ar": "🇸🇦",
    "ara": "🇸🇦",
    "he": "🇮🇱",
    "heb": "🇮🇱",
    "th": "🇹🇭",
    "tha": "🇹🇭",
    "vi": "🇻🇳",
    "vie": "🇻🇳",
    "id": "🇮🇩",
    "ind": "🇮🇩",
    "mul": "🌐",
    "multi": "🌐",
    "und": "❓",
}

SIZE_UNIT = ("B", "KB", "MB", "GB", "TB")


def get_language_flag(lang_code: str) -> str:
    code = lang_code.lower().strip()
    return LANGUAGE_TO_FLAG.get(code, f"[{code.upper()}]")


def format_size(size: float) -> str:
    i = 0
    while size >= 1024:
        size = size / 1024
        i += 1

    return f"{size:.2f}{SIZE_UNIT[min(i, len(SIZE_UNIT) - 1)]}"
