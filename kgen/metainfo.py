SPECIAL = [
    "1girl",
    "2girls",
    "3girls",
    "4girls",
    "5girls",
    "6+girls",
    "multiple girls",
    "1boy",
    "2boys",
    "3boys",
    "4boys",
    "5boys",
    "6+boys",
    "multiple boys",
    "male focus",
    "1other",
    "2others",
    "3others",
    "4others",
    "5others",
    "6+others",
    "multiple others",
]
POSSIBLE_QUALITY_TAGS = [
    "masterpiece",
    "best quality",
    "great quality",
    "good quality",
    "normal quality",
    "low quality",
    "worse quality",
    "very aesthetic",
    "aesthetic",
    "displeasing",
    "very displeasing",
    "newest",
    "recent",
    "mid",
    "early",
    "old",
    "score_9",
    "score_8_up",
    "score_7_up",
    "score_6_up",
    "score_5_up",
    "score_4_up",
    "source_anime",
    "source_cartoon",
    "source_furry",
    "source_pony",
]
RATING_TAGS = ["safe", "general", "sfw", "sensitive", "nsfw", "explicit"]

# minimum length of generated contents
# unit: tags
TARGET = {
    "very_short": 8,
    "short": 16,
    "long": 32,
    "very_long": 48,
}
TARGET_TITPOP = {
    "very_short": 6,
    "short": 18,
    "long": 36,
    "very_long": 54,
}
# unit: sentences
TARGET_TITPOP_NL = {
    "very_short": 1,
    "short": 2,
    "long": 4,
    "very_long": 6,
}
