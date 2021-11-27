#!/usr/bin/python3
# -*- coding: utf-8 -*-
# key-mapper - GUI for device specific keyboard mappings
# Copyright (C) 2021 sezanzeb <proxima@sezanzeb.de>
#
# This file is part of key-mapper.
#
# key-mapper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# key-mapper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with key-mapper.  If not, see <https://www.gnu.org/licenses/>.


"""A set of all human readable symbols xkb understands.

They are case sensitive.
"""

# https://gist.github.com/sezanzeb/1236917f509f13d30010c98c9fa8389f
VALID_XKB_SYMBOLS = {
    "Cyrillic_ve",
    "parenleft",
    "SunVideoLowerBrightness",
    "KP_6",
    "Q",
    "uparrow",
    "Cyrillic_yu",
    "Sinh_ca",
    "Cyrillic_YA",
    "Thai_ru",
    "dead_belowdot",
    "XF86Keyboard",
    "zacute",
    "Greek_beta",
    "Greek_PSI",
    "Sinh_cha",
    "XF86AudioMicMute",
    "Shift_Lock",
    "onesixth",
    "Kana_Lock",
    "Cyrillic_zhe_descender",
    "Arabic_ddal",
    "iacute",
    "Greek_kappa",
    "W",
    "Ooblique",
    "dead_stroke",
    "Sinh_oo",
    "dollar",
    "Arabic_comma",
    "hebrew_yod",
    "V",
    "egrave",
    "hpDeleteLine",
    "Undo",
    "Armenian_tyun",
    "Armenian_exclam",
    "Arabic_keheh",
    "Greek_omega",
    "includedin",
    "partialderivative",
    "Arabic_ha",
    "Otilde",
    "Sinh_ai",
    "Georgian_tar",
    "Serbian_TSHE",
    "Thai_saraaimaimalai",
    "Eabovedot",
    "F25",
    "downarrow",
    "Arabic_tehmarbuta",
    "doubledagger",
    "Armenian_NU",
    "kana_RE",
    "w",
    "Sinh_ng",
    "XF86Terminal",
    "kana_fullstop",
    "Ukrainin_ie",
    "Sinh_pha",
    "dead_belowmacron",
    "Arabic_beh",
    "Ugrave",
    "plusminus",
    "thorn",
    "nobreakspace",
    "seveneighths",
    "Arabic_rreh",
    "XF86LaunchA",
    "oe",
    "nabla",
    "Cyrillic_che",
    "XF86AudioLowerVolume",
    "kana_O",
    "uprightcorner",
    "KP_Equal",
    "scedilla",
    "tslash",
    "bar",
    "Armenian_ligature_ew",
    "Byelorussian_SHORTU",
    "Scircumflex",
    "Num_Lock",
    "kana_NO",
    "Georgian_in",
    "KP_Add",
    "braceleft",
    "SunFA_Tilde",
    "Cyrillic_u_straight",
    "Sinh_la",
    "F24",
    "Ukrainian_ghe_with_upturn",
    "Greek_upsilon",
    "XF86AddFavorite",
    "y",
    "Georgian_chin",
    "ellipsis",
    "leftarrow",
    "asciicircum",
    "Greek_UPSILON",
    "Armenian_apostrophe",
    "Georgian_en",
    "XF86Spell",
    "L6",
    "ograve",
    "approxeq",
    "kana_RU",
    "Cyrillic_JE",
    "XF86Launch5",
    "Cyrillic_EF",
    "hebrew_mem",
    "Arabic_waw",
    "eth",
    "Cyrillic_ghe",
    "Georgian_gan",
    "kana_yo",
    "KP_7",
    "hebrew_bet",
    "Ukrainian_GHE_WITH_UPTURN",
    "seconds",
    "bott",
    "Greek_theta",
    "Thai_thothahan",
    "Sinh_tha",
    "h",
    "Armenian_tsa",
    "dead_abovedot",
    "Arabic_heh_goal",
    "XF86LaunchD",
    "logicalor",
    "Armenian_ben",
    "KP_Begin",
    "Gabovedot",
    "Armenian_SHA",
    "Arabic_meem",
    "dead_currency",
    "Cancel",
    "fabovedot",
    "Cyrillic_be",
    "C",
    "XF86Cut",
    "q",
    "Uacute",
    "Cyrillic_LJE",
    "thinspace",
    "Thai_chochoe",
    "Thai_sarauu",
    "XF86ModeLock",
    "Armenian_VEV",
    "Cyrillic_KA_vertstroke",
    "XF86Messenger",
    "Sinh_fa",
    "Greek_ZETA",
    "Cyrillic_i_macron",
    "Agrave",
    "Cyrillic_nje",
    "SunFA_Circum",
    "Scaron",
    "Sinh_ya",
    "XF86TouchpadOff",
    "Cyrillic_el",
    "Scedilla",
    "Armenian_DZA",
    "rcaron",
    "fiveeighths",
    "Romaji",
    "Sinh_ba",
    "Sinh_ri",
    "Cyrillic_schwa",
    "EuroSign",
    "SunPaste",
    "diamond",
    "XF86WWAN",
    "Thai_lekhok",
    "Cyrillic_zhe",
    "Cyrillic_KA",
    "F34",
    "Cyrillic_yeru",
    "Thai_totao",
    "SunFA_Cedilla",
    "XF86Reply",
    "F31",
    "Aogonek",
    "kana_SA",
    "Armenian_TCHE",
    "hebrew_kaph",
    "XF86RotationLockToggle",
    "Sinh_dhha",
    "KP_2",
    "Ccircumflex",
    "s",
    "Cyrillic_SHA",
    "Greek_EPSILON",
    "XF86Search",
    "Ukrainian_yi",
    "Escape",
    "uacute",
    "Armenian_lyun",
    "XF86Tools",
    "cabovedot",
    "ocircumflex",
    "Ohorn",
    "kana_WO",
    "equal",
    "Arabic_lam",
    "Thai_soso",
    "F3",
    "Sinh_ka",
    "Thai_sarao",
    "dead_belowring",
    "F33",
    "braille_dot_6",
    "Thai_saraam",
    "Arabic_hamza_above",
    "Lcaron",
    "Farsi_1",
    "Georgian_an",
    "tabovedot",
    "omacron",
    "m",
    "logicaland",
    "u",
    "Multi_key",
    "Sinh_na",
    "F28",
    "hebrew_he",
    "SunOpen",
    "exclam",
    "XF86Support",
    "kana_MA",
    "dead_doublegrave",
    "SeeNkeyinSAXlayout",
    "Thai_ngongu",
    "Cyrillic_SOFTSIGN",
    "Thai_yoying",
    "dead_doubleacute",
    "T",
    "Cyrillic_io",
    "Group1",
    "Armenian_zhe",
    "Arabic_4",
    "prolongedsound",
    "L4",
    "Sinh_lu2",
    "Cyrillic_CHE_descender",
    "dead_breve",
    "hebrew_zade",
    "Amacron",
    "hstroke",
    "Cyrillic_EL",
    "zerosubscript",
    "Thai_khokhai",
    "parenright",
    "Thai_thothong",
    "XF86Go",
    "numbersign",
    "greaterthanequal",
    "KP_9",
    "Thai_maitaikhu",
    "Arabic_0",
    "hebrew_finalpe",
    "Armenian_to",
    "Arabic_1",
    "ampersand",
    "THORN",
    "Arabic_ain",
    "Eth",
    "XF86Meeting",
    "Sinh_au",
    "Arabic_3",
    "j",
    "F26",
    "Sinh_rii",
    "Thai_saraa",
    "L9",
    "Arabic_percent",
    "Home",
    "Farsi_6",
    "Sinh_u",
    "backslash",
    "Greek_nu",
    "Cyrillic_i",
    "XF86ScrollUp",
    "jcircumflex",
    "cent",
    "Cyrillic_shcha",
    "umacron",
    "Omacron",
    "Armenian_VYUN",
    "Thai_sosala",
    "Cyrillic_es",
    "Arabic_alef",
    "6",
    "KP_Tab",
    "KP_Insert",
    "Armenian_ra",
    "eogonek",
    "Eacute",
    "leftdoublequotemark",
    "Eisu_toggle",
    "division",
    "Arabic_damma",
    "schwa",
    "similarequal",
    "XF86MonBrightnessCycle",
    "Armenian_JE",
    "Thai_maitho",
    "Thai_thonangmontho",
    "grave",
    "Greek_GAMMA",
    "Return",
    "Thai_leksi",
    "Cyrillic_HARDSIGN",
    "Arabic_question_mark",
    "Armenian_LYUN",
    "kana_MI",
    "B",
    "identical",
    "dead_invertedbreve",
    "Sinh_i2",
    "diaeresis",
    "Tcedilla",
    "lowrightcorner",
    "XF86WakeUp",
    "F23",
    "E",
    "Sinh_ttha",
    "Pabovedot",
    "Greek_IOTA",
    "Nosymbol",
    "sacute",
    "Cyrillic_E",
    "Mode_switch",
    "hebrew_dalet",
    "Yacute",
    "asterisk",
    "Armenian_ken",
    "Thai_dodek",
    "kana_TE",
    "lstroke",
    "Armenian_KE",
    "XF86_Ungrab",
    "SeeNkey",
    "Thai_saraue",
    "Thai_maiyamok",
    "hpSystem",
    "Arabic_dammatan",
    "Greek_lambda",
    "Touroku",
    "Cyrillic_u",
    "L7",
    "U",
    "downtack",
    "Arabic_yeh_baree",
    "oacute",
    "XF86DOS",
    "Georgian_don",
    "Georgian_on",
    "XF86Favorites",
    "p",
    "braille_dot_4",
    "Redo",
    "Georgian_phar",
    "agrave",
    "Caps_Lock",
    "KP_3",
    "Cyrillic_GHE_bar",
    "SunFA_Acute",
    "ssharp",
    "slash",
    "Armenian_HI",
    "infinity",
    "Thai_sarauee",
    "XF86Paste",
    "Thai_lakkhangyao",
    "Armenian_INI",
    "XF86UserPB",
    "eightsuperior",
    "ibreve",
    "XF86Reload",
    "XF86MenuPB",
    "Armenian_tso",
    "Sinh_aee",
    "Greek_gamma",
    "Armenian_accent",
    "udoubleacute",
    "L1",
    "vertbar",
    "kana_MU",
    "XF86LightBulb",
    "Acircumflex",
    "Sinh_ru2",
    "Dstroke",
    "Armenian_yech",
    "n",
    "Sinh_luu",
    "2",
    "Sinh_e",
    "Ecircumflex",
    "dead_dasia",
    "singlelowquotemark",
    "overbar",
    "Arabic_ra",
    "Menu",
    "Arabic_yeh",
    "Mabovedot",
    "XF86New",
    "Georgian_har",
    "Sinh_luu2",
    "SunAudioMute",
    "L8",
    "hebrew_qoph",
    "upstile",
    "Cyrillic_SHCHA",
    "KP_F3",
    "union",
    "EuroS",
    "Cyrillic_ZE",
    "trademark",
    "XF86MyComputer",
    "Arabic_gaf",
    "hebrew_aleph",
    "SunCopy",
    "ae",
    "Sinh_ai2",
    "Armenian_men",
    "ISO_Next_Group",
    "lowleftcorner",
    "Zabovedot",
    "Rcedilla",
    "dagger",
    "Arabic_khah",
    "Armenian_PYUR",
    "Sinh_ddha",
    "Sinh_ma",
    "F",
    "F19",
    "Thai_nonen",
    "kana_TA",
    "guillemotleft",
    "eng",
    "Ibreve",
    "Cyrillic_HA_descender",
    "Pause",
    "XF86Launch0",
    "Arabic_tteh",
    "hebrew_ayin",
    "kana_RA",
    "Cyrillic_U",
    "Sinh_au2",
    "dcaron",
    "Georgian_jhan",
    "onethird",
    "Gcedilla",
    "Thai_maiek",
    "Sinh_o",
    "XF86ZoomIn",
    "kana_KU",
    "kana_A",
    "XF86Launch9",
    "Sinh_mba",
    "Arabic_hamzaonyeh",
    "dead_iota",
    "Ukrainian_I",
    "dead_grave",
    "Cyrillic_GHE",
    "trigraph_C_H",
    "Fabovedot",
    "Sinh_jnya",
    "Thai_saraae",
    "Cyrillic_TSE",
    "Cyrillic_SHORTI",
    "Armenian_CHA",
    "Cyrillic_ghe_bar",
    "Sinh_nna",
    "Arabic_theh",
    "Cyrillic_ef",
    "Farsi_8",
    "KP_4",
    "scaron",
    "dead_comma",
    "kana_NI",
    "c",
    "8",
    "Arabic_sukun",
    "dead_belowcomma",
    "Armenian_khe",
    "degree",
    "Greek_MU",
    "ncaron",
    "Georgian_zhar",
    "acircumflex",
    "F35",
    "colon",
    "hpInsertLine",
    "Imacron",
    "jot",
    "babovedot",
    "Sinh_aa",
    "ISO_Left_Tab",
    "XF86MonBrightnessUp",
    "KP_Subtract",
    "Cyrillic_tse",
    "KP_0",
    "Utilde",
    "Cyrillic_hardsign",
    "Thai_saraaa",
    "malesymbol",
    "kana_SE",
    "Arabic_9",
    "zerosuperior",
    "acute",
    "Arabic_kasra",
    "Armenian_e",
    "Farsi_3",
    "crossinglines",
    "Armenian_za",
    "OE",
    "k",
    "Igrave",
    "Armenian_pyur",
    "kana_HO",
    "dead_circumflex",
    "onesuperior",
    "XF86AudioPrev",
    "Ukrainian_YI",
    "Sinh_ssha",
    "KP_Multiply",
    "Arabic_7",
    "4",
    "mu",
    "yacute",
    "N",
    "Sinh_bha",
    "Georgian_qar",
    "Armenian_tche",
    "Tslash",
    "enfilledcircbullet",
    "none",
    "XF86TaskPane",
    "kana_NU",
    "Cyrillic_U_macron",
    "Udiaeresis",
    "Ntilde",
    "Armenian_FE",
    "idotless",
    "Cyrillic_ze",
    "nacute",
    "hebrew_nun",
    "Sinh_ee",
    "emacron",
    "Thai_sarau",
    "hpClearLine",
    "Georgian_un",
    "Greek_OMEGA",
    "XF86Finance",
    "braille_dot_7",
    "rightcaret",
    "Cyrillic_pe",
    "gcaron",
    "Armenian_YECH",
    "Cyrillic_dzhe",
    "kana_comma",
    "XF86PowerOff",
    "Armenian_RA",
    "5",
    "XF86iTouch",
    "quote",
    "Macedonia_dse",
    "semivoicedsound",
    "SunStop",
    "macron",
    "XF86Music",
    "gabovedot",
    "oslash",
    "Armenian_TYUN",
    "Sinh_e2",
    "Ukrainian_ie",
    "Sinh_jha",
    "XF86News",
    "ISO_Level5_Shift",
    "z",
    "J",
    "dead_horn",
    "Greek_iota",
    "Arabic_heh",
    "Ncedilla",
    "function",
    "Dabovedot",
    "Cyrillic_em",
    "Georgian_nar",
    "noSymbol",
    "idiaeresis",
    "Cyrillic_softsign",
    "Cyrillic_che_vertstroke",
    "Armenian_SE",
    "XF86ScrollDown",
    "hebrew_resh",
    "hebrew_pe",
    "Kcedilla",
    "udiaeresis",
    "paragraph",
    "kana_o",
    "r",
    "aogonek",
    "utilde",
    "Cyrillic_en_descender",
    "XF86MenuKB",
    "Cyrillic_u_straight_bar",
    "XF86Launch3",
    "XF86Market",
    "hebrew_lamed",
    "kana_YU",
    "Armenian_AT",
    "Thai_thanthakhat",
    "Armenian_TSO",
    "Control_R",
    "Muhenkan",
    "XF86LaunchF",
    "Arabic_superscript_alef",
    "XF86User1KB",
    "KP_Decimal",
    "Sinh_pa",
    "Serbian_tshe",
    "Sinh_ruu2",
    "Oacute",
    "odoubleacute",
    "Arabic_semicolon",
    "doubleacute",
    "Greek_finalsmallsigma",
    "XF86FullScreen",
    "abreve",
    "apLineDel",
    "Super_R",
    "Arabic_tatweel",
    "SunAgain",
    "XF86Stop",
    "periodcentered",
    "Cyrillic_ER",
    "Ukrainian_i",
    "VoidSymbol",
    "Arabic_veh",
    "numerosign",
    "Armenian_cha",
    "at",
    "Armenian_GHAT",
    "Aogonekl",
    "ugrave",
    "F8",
    "racute",
    "hebrew_shin",
    "XF86Back",
    "Egrave",
    "Sinh_ng2",
    "SunFront",
    "Thai_leksam",
    "Cyrillic_ES",
    "kana_tsu",
    "F17",
    "ISO_Level5_Latch",
    "XF86Start",
    "Armenian_dza",
    "SCHWA",
    "Armenian_da",
    "Arabic_madonalef",
    "hebrew_waw",
    "Thai_hohip",
    "Thai_fofan",
    "Tcaron",
    "onequarter",
    "cedilla",
    "Arabic_feh",
    "Cyrillic_DZHE",
    "amacron",
    "Greek_rho",
    "Cyrillic_KA_descender",
    "notelementof",
    "Zenkaku_Hankaku",
    "K",
    "XF86Phone",
    "Thai_sarai",
    "kana_ME",
    "9",
    "F6",
    "F13",
    "Cyrillic_a",
    "Armenian_vo",
    "Cyrillic_EN",
    "Greek_SIGMA",
    "Shift_R",
    "heart",
    "XF86Shop",
    "kana_SHI",
    "Armenian_hyphen",
    "Sinh_ndha",
    "Nacute",
    "kana_conjunctive",
    "hcircumflex",
    "Cyrillic_DE",
    "Find",
    "integral",
    "f",
    "leftsinglequotemark",
    "XF86Send",
    "uring",
    "SunSys_Req",
    "Sinh_u2",
    "Print",
    "hebrew_gimel",
    "notequal",
    "kana_HA",
    "Sinh_nya",
    "Itilde",
    "kana_yu",
    "XF86TouchpadOn",
    "Sinh_ae",
    "Rcaron",
    "Udoubleacute",
    "b",
    "kana_SO",
    "L10",
    "ccedilla",
    "aacute",
    "Ograve",
    "hebrew_samech",
    "Sinh_gha",
    "Y",
    "Thai_lekha",
    "less",
    "SunFA_Grave",
    "SunAudioLowerVolume",
    "Cyrillic_ha",
    "Sinh_nja",
    "Arabic_sad",
    "iogonek",
    "Adiaeresis",
    "Greek_delta",
    "Cyrillic_shha",
    "hpInsertChar",
    "rightanglebracket",
    "Georgian_zen",
    "Georgian_can",
    "Kanji",
    "ecaron",
    "SunCut",
    "Greek_KAPPA",
    "kana_i",
    "ydiaeresis",
    "Georgian_khar",
    "foursuperior",
    "emptyset",
    "Sinh_kha",
    "kana_KO",
    "Arabic_heh_doachashmee",
    "Ocircumflex",
    "ucircumflex",
    "squareroot",
    "Cyrillic_che_descender",
    "kcedilla",
    "enopencircbullet",
    "Hiragana",
    "Arabic_fullstop",
    "braille_dot_9",
    "XF86Mail",
    "KP_1",
    "XF86Clear",
    "Hangul",
    "Sinh_ja",
    "breve",
    "threeeighths",
    "Armenian_ghat",
    "Armenian_TO",
    "Thai_thothan",
    "Greek_sigma",
    "Thai_maihanakat",
    "ISO_Level3_Lock",
    "Arabic_noon_ghunna",
    "Armenian_O",
    "KP_Enter",
    "kana_U",
    "Ydiaeresis",
    "Cyrillic_O",
    "greater",
    "quotedbl",
    "Georgian_xan",
    "Thai_sarae",
    "kana_KA",
    "Alt_R",
    "threequarters",
    "G",
    "Armenian_re",
    "XF86RFKill",
    "g",
    "Sinh_thha",
    "Aring",
    "Cyrillic_A",
    "Thai_topatak",
    "leftradical",
    "ubreve",
    "Gbreve",
    "Georgian_shin",
    "Ecaron",
    "Cyrillic_U_straight",
    "Thai_lekkao",
    "masculine",
    "XF86Community",
    "rcedilla",
    "Thai_kokai",
    "Cyrillic_EN_descender",
    "Sinh_ha",
    "XF86Sleep",
    "topt",
    "Iogonek",
    "Thai_khokhon",
    "Greek_eta",
    "guilsinglright",
    "Thai_nonu",
    "upleftcorner",
    "Z",
    "Cyrillic_ha_descender",
    "currency",
    "XF86RotationKB",
    "Hstroke",
    "XF86Travel",
    "XF86Display",
    "XF86ContrastAdjust",
    "Georgian_he",
    "Greek_alpha",
    "bracketright",
    "Iacute",
    "Greek_DELTA",
    "XF86_Next_VMode",
    "Farsi_0",
    "Super_L",
    "Greek_OMICRON",
    "ISO_Group_Latch",
    "Arabic_fathatan",
    "Sinh_sha",
    "Georgian_las",
    "XF86LaunchB",
    "Armenian_o",
    "dead_diaeresis",
    "SeeBkey",
    "Cyrillic_I_macron",
    "Cyrillic_ZHE",
    "Macedonia_DSE",
    "Sinh_oo2",
    "F5",
    "hebrew_chet",
    "Georgian_kan",
    "ncedilla",
    "Uring",
    "kana_u",
    "dstroke",
    "trigraph_c_h",
    "Greek_tau",
    "Georgian_ban",
    "Arabic_hamzaunderalef",
    "i",
    "Thai_sosua",
    "kana_E",
    "fivesuperior",
    "gcircumflex",
    "Hyper_L",
    "abovedot",
    "Thai_chochang",
    "minutes",
    "kana_KI",
    "Armenian_TSA",
    "NoSymbol",
    "dead_abovering",
    "XF86KbdBrightnessUp",
    "sixsuperior",
    "Sinh_uu2",
    "Help",
    "radical",
    "Armenian_vev",
    "kana_I",
    "uhorn",
    "kana_YO",
    "Cyrillic_TE",
    "XF86WWW",
    "Pointer_EnableKeys",
    "Arabic_tah",
    "gbreve",
    "Katakana",
    "Serbian_DJE",
    "A",
    "Cyrillic_ie",
    "ogonek",
    "XF86_Prev_VMode",
    "Greek_chi",
    "Cyrillic_VE",
    "Cyrillic_o_bar",
    "XF86Close",
    "1",
    "quoteright",
    "Arabic_hamza",
    "Henkan_Mode",
    "KP_Suptract",
    "Idiaeresis",
    "Georgian_par",
    "ISO_Level3_Shift",
    "XF86VendorHome",
    "F9",
    "Hiragana_Katakana",
    "ifonlyif",
    "Armenian_DA",
    "SeeBkeyinSAXlayout",
    "Farsi_9",
    "lcedilla",
    "v",
    "questiondown",
    "Macedonia_kje",
    "dead_tilde",
    "Armenian_MEN",
    "P",
    "Cyrillic_sha",
    "scircumflex",
    "femalesymbol",
    "copyright",
    "kana_HI",
    "kana_TO",
    "KP_8",
    "kana_ya",
    "7",
    "Sinh_a",
    "emdash",
    "Farsi_2",
    "XF86Excel",
    "Arabic_fatha",
    "yen",
    "kana_WA",
    "Cyrillic_ka_vertstroke",
    "XF86Bluetooth",
    "eabovedot",
    "kana_MO",
    "DongSign",
    "Dcaron",
    "Delete",
    "Control_L",
    "Sabovedot",
    "SunUndo",
    "group1",
    "Sinh_dha",
    "XF86HotLinks",
    "ordfeminine",
    "Greek_epsilon",
    "percent",
    "KP_Home",
    "Arabic_5",
    "rightsinglequotemark",
    "Umacron",
    "kana_TSU",
    "guillemotright",
    "lacute",
    "F32",
    "Arabic_maddaonalef",
    "Georgian_rae",
    "Cyrillic_er",
    "Greek_PI",
    "Odoubleacute",
    "Thai_leksong",
    "Georgian_jil",
    "F30",
    "XF86Launch4",
    "Byelorussian_shortu",
    "kana_NA",
    "Sinh_i",
    "Sinh_h2",
    "XF86Pictures",
    "ISO_Level5_Lock",
    "XF86KbdBrightnessDown",
    "XF86Eject",
    "Georgian_we",
    "brokenbar",
    "XF86ScreenSaver",
    "Armenian_ini",
    "KP_Prior",
    "hpDeleteChar",
    "Arabic_kaf",
    "o",
    "XF86Calendar",
    "Cyrillic_SCHWA",
    "F18",
    "F29",
    "ooblique",
    "Greek_phi",
    "Armenian_ayb",
    "Arabic_ghain",
    "Armenian_fe",
    "Armenian_sha",
    "F15",
    "Thai_lekchet",
    "elementof",
    "intersection",
    "Thai_loling",
    "Jcircumflex",
    "Georgian_tan",
    "Ncaron",
    "kana_a",
    "Eisu_Shift",
    "comma",
    "permille",
    "Cyrillic_CHE_vertstroke",
    "Armenian_at",
    "Uogonek",
    "Thai_leksun",
    "Sacute",
    "minus",
    "Cyrillic_PE",
    "kana_middledot",
    "XF86LaunchE",
    "braille_dot_10",
    "Armenian_AYB",
    "doublequote",
    "XF86KbdLightOnOff",
    "dead_abovecomma",
    "XF86History",
    "SunVideoRaiseBrightness",
    "Arabic_noon",
    "imacron",
    "a",
    "Cyrillic_U_straight_bar",
    "F16",
    "dead_belowcircumflex",
    "Thai_maitri",
    "Armenian_full_stop",
    "Icircumflex",
    "Ccaron",
    "Cyrillic_ZHE_descender",
    "any",
    "odiaeresis",
    "XF86Hibernate",
    "sabovedot",
    "Arabic_seen",
    "Lcedilla",
    "Prior",
    "SunFA_Diaeresis",
    "Armenian_nu",
    "XF86AudioRewind",
    "Babovedot",
    "XF86AudioPlay",
    "X",
    "KP_Up",
    "I",
    "lessthanequal",
    "XF86AudioNext",
    "R",
    "Cyrillic_CHE",
    "Greek_LAMDA",
    "Cyrillic_HA",
    "horizconnector",
    "KP_End",
    "End",
    "approximate",
    "Arabic_kasratan",
    "caret",
    "F22",
    "kana_N",
    "hebrew_finalnun",
    "dead_ogonek",
    "Arabic_zah",
    "doublelowquotemark",
    "Greek_PHI",
    "dead_caron",
    "XF86MonBrightnessDown",
    "ediaeresis",
    "Thai_sorusi",
    "XF86ToDoList",
    "F1",
    "XF86OfficeHome",
    "period",
    "Select",
    "ISO_First_Group",
    "Armenian_je",
    "Greek_CHI",
    "otilde",
    "Sinh_ee2",
    "Thai_leknung",
    "Georgian_hie",
    "KP_Left",
    "KP_Separator",
    "F21",
    "question",
    "trigraph_C_h",
    "Armenian_VO",
    "onehalf",
    "Georgian_ghan",
    "club",
    "Georgian_cil",
    "Arabic_hamza_below",
    "XF86HomePage",
    "Arabic_alefmaksura",
    "ohorn",
    "twosuperior",
    "Greek_pi",
    "guilsinglleft",
    "KP_Divide",
    "Cyrillic_de",
    "F4",
    "Sinh_ra",
    "rightarrow",
    "ninesuperior",
    "XF86Launch8",
    "adiaeresis",
    "endash",
    "Greek_lamda",
    "Linefeed",
    "Armenian_ho",
    "XF86AudioForward",
    "dead_greek",
    "Armenian_RE",
    "XF86AudioRaiseVolume",
    "XF86RotationPB",
    "pabovedot",
    "Cyrillic_NJE",
    "Right",
    "Thai_wowaen",
    "Gcaron",
    "wacute",
    "t",
    "Thai_thothung",
    "XF86OpenURL",
    "leftanglebracket",
    "voicedsound",
    "icircumflex",
    "XF86Q",
    "XF86Documents",
    "Zacute",
    "KP_F4",
    "Cyrillic_e",
    "Cyrillic_ya",
    "KP_F1",
    "Henkan",
    "Armenian_ZA",
    "caron",
    "Next",
    "Ubreve",
    "underscore",
    "0",
    "aring",
    "Racute",
    "XF86Video",
    "ISO_Last_Group",
    "Hangul_Hanja",
    "Thai_lekpaet",
    "kana_e",
    "XF86Book",
    "Cyrillic_SHHA",
    "Armenian_pe",
    "Serbian_dje",
    "Arabic_2",
    "Armenian_GIM",
    "Massyo",
    "Greek_TAU",
    "XF86ApplicationLeft",
    "Oslash",
    "Arabic_hamzaonalef",
    "leftt",
    "XF86User2KB",
    "Arabic_jeem",
    "itilde",
    "kana_FU",
    "Sinh_lla",
    "L",
    "F14",
    "XF86Standby",
    "Clear",
    "Up",
    "Arabic_6",
    "dead_psili",
    "Georgian_san",
    "Meta_L",
    "kana_KE",
    "Arabic_madda_above",
    "S",
    "Sinh_kunddaliya",
    "XF86Away",
    "XF86Battery",
    "Thai_rorua",
    "bracketleft",
    "cacute",
    "Cacute",
    "XF86Xfer",
    "F20",
    "XF86ApplicationRight",
    "multiply",
    "Armenian_separation_mark",
    "dead_macron",
    "Macedonia_gje",
    "leftcaret",
    "L5",
    "ISO_Prev_Group",
    "braille_dot_1",
    "Arabic_thal",
    "sterling",
    "Cyrillic_je",
    "Armenian_se",
    "Georgian_man",
    "braceright",
    "XF86Forward",
    "dead_longsolidusoverlay",
    "Cyrillic_o",
    "Thai_saraaimaimuan",
    "digraph_Ch",
    "XF86Game",
    "KP_Down",
    "XF86_ClearGrab",
    "Macedonia_KJE",
    "Farsi_5",
    "Thai_moma",
    "Cyrillic_ka",
    "hebrew_taw",
    "F11",
    "Thai_thophuthao",
    "Greek_XI",
    "igrave",
    "plus",
    "l",
    "Greek_BETA",
    "Alt_L",
    "Armenian_KHE",
    "gcedilla",
    "zabovedot",
    "Cyrillic_I",
    "Thai_phophan",
    "Arabic_shadda",
    "kana_SU",
    "Thai_chochan",
    "Greek_ETA",
    "Thai_khokhuat",
    "uogonek",
    "Armenian_HO",
    "XF86AudioPreset",
    "XF86Suspend",
    "Break",
    "Georgian_vin",
    "D",
    "Thai_baht",
    "Arabic_dad",
    "Armenian_BEN",
    "Atilde",
    "Greek_xi",
    "F10",
    "XF86TouchpadToggle",
    "Thai_honokhuk",
    "kana_openingbracket",
    "XF86AudioMute",
    "Uhorn",
    "question_mark",
    "Greek_mu",
    "Georgian_char",
    "rightdoublequotemark",
    "kana_HE",
    "Georgian_hae",
    "KP_Next",
    "Thai_choching",
    "Cyrillic_en",
    "XF86SplitScreen",
    "XF86AudioPause",
    "F27",
    "Macedonia_GJE",
    "ETH",
    "eacute",
    "partialderivate",
    "XF86RotateWindows",
    "XF86Launch2",
    "F2",
    "threesubscript",
    "digraph_ch",
    "ezh",
    "Lacute",
    "Armenian_KEN",
    "XF86WebCam",
    "Armenian_E",
    "Sinh_ii",
    "Cyrillic_YU",
    "Sinh_tta",
    "variation",
    "O",
    "Armenian_gim",
    "Aacute",
    "Arabic_jeh",
    "Tabovedot",
    "hyphen",
    "XF86Launch6",
    "Sinh_uu",
    "hebrew_zain",
    "braille_dot_5",
    "Greek_THETA",
    "F12",
    "Cyrillic_lje",
    "Iabovedot",
    "dead_belowbreve",
    "3",
    "Arabic_dal",
    "Thai_yoyak",
    "Greek_omicron",
    "mabovedot",
    "XF86Save",
    "XF86ScrollClick",
    "kana_CHI",
    "Cyrillic_shorti",
    "hebrew_finalmem",
    "XF86BrightnessAdjust",
    "Thai_lochula",
    "Sinh_lu",
    "Armenian_vyun",
    "Greek_psi",
    "Zcaron",
    "Hyper_R",
    "kana_NE",
    "XF86AudioStop",
    "lcaron",
    "quoteleft",
    "Arabic_hamzaonwaw",
    "rightt",
    "Cyrillic_te",
    "twosubscript",
    "Ukrainian_IE",
    "atilde",
    "registered",
    "Ccedilla",
    "L3",
    "Sinh_aa2",
    "Thai_khorakhang",
    "x",
    "Eogonek",
    "KP_Delete",
    "XF86BackForward",
    "Tab",
    "Sinh_aee2",
    "XF86Open",
    "Cabovedot",
    "Gcircumflex",
    "Execute",
    "KP_Right",
    "Thai_maichattawa",
    "Cyrillic_u_macron",
    "Greek_zeta",
    "Farsi_yeh",
    "KP_5",
    "e",
    "Thai_nikhahit",
    "Greek_NU",
    "braille_dot_3",
    "Arabic_sheen",
    "ccircumflex",
    "Thai_khokhwai",
    "Cyrillic_ka_descender",
    "dead_cedilla",
    "XF86Copy",
    "dabovedot",
    "Down",
    "XF86Launch1",
    "XF86Explorer",
    "Thai_bobaimai",
    "H",
    "Thai_phinthu",
    "apostrophe",
    "Cyrillic_YERU",
    "L2",
    "hebrew_finalzade",
    "Arabic_zain",
    "XF86LogOff",
    "M",
    "Armenian_hi",
    "Sinh_ae2",
    "Sinh_o2",
    "Shift_L",
    "Sinh_ndda",
    "SunProps",
    "voidsymbol",
    "Farsi_4",
    "XF86AudioRecord",
    "Cyrillic_O_bar",
    "Insert",
    "Greek_LAMBDA",
    "ENG",
    "Scroll_Lock",
    "XF86LaunchC",
    "ecircumflex",
    "XF86MailForward",
    "BackSpace",
    "Arabic_hah",
    "Sinh_al",
    "SunFind",
    "Arabic_8",
    "section",
    "Lstroke",
    "Armenian_ZHE",
    "braille_dot_8",
    "Thai_lu",
    "XF86WLAN",
    "Sinh_sa",
    "semicolon",
    "Georgian_fi",
    "Arabic_teh",
    "Thai_phophung",
    "Cyrillic_EM",
    "therefore",
    "XF86Word",
    "Cyrillic_BE",
    "Farsi_7",
    "Thai_popla",
    "Armenian_PE",
    "zcaron",
    "Meta_R",
    "horizlinescan5",
    "hebrew_tet",
    "dead_acute",
    "XF86ZoomOut",
    "Armenian_question",
    "Odiaeresis",
    "KP_F2",
    "braille_dot_2",
    "Cyrillic_IO",
    "Arabic_tcheh",
    "Armenian_ke",
    "kra",
    "sevensuperior",
    "includes",
    "Thai_oang",
    "XF86Calculator",
    "tcaron",
    "Georgian_hoe",
    "onesubscript",
    "kana_RO",
    "Cyrillic_IE",
    "threesuperior",
    "d",
    "Greek_ALPHA",
    "Greek_horizbar",
    "XF86Launch7",
    "AE",
    "Thorn",
    "Thai_paiyannoi",
    "dead_hook",
    "F7",
    "Sinh_va",
    "EZH",
    "Wacute",
    "Ucircumflex",
    "Thai_phosamphao",
    "downstile",
    "Sinh_nga",
    "Arabic_peh",
    "Hcircumflex",
    "NewSheqelSign",
    "kana_YA",
    "ccaron",
    "Sinh_ga",
    "kana_closingbracket",
    "asciitilde",
    "notsign",
    "XF86AudioMedia",
    "Left",
    "Abreve",
    "underbar",
    "Sinh_ii2",
    "Arabic_qaf",
    "ISO_Level3_Latch",
    "SunVideoDegauss",
    "Ediaeresis",
    "space",
    "Sinh_dda",
    "ntilde",
    "Thai_fofa",
    "XF86CD",
    "exclamdown",
    "oneeighth",
    "Emacron",
    "kana_RI",
    "hebrew_finalkaph",
    "digraph_CH",
    "tcedilla",
    "Thai_saraii",
    "SunAudioRaiseVolume",
    "Thai_dochada",
    "Greek_RHO",
}
