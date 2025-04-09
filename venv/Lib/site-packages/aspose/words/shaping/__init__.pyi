import aspose.words
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable, List
from enum import Enum

class BasicTextShaperCache:
    """Implements basic cache for :class:`ITextShaper` instances. This class is thread-safe."""
    
    def __init__(self, factory: aspose.words.shaping.ITextShaperFactory):
        """Wraps *factory* and caches:meth:`ITextShaperFactory.get_text_shaper` results."""
        ...
    
    ...

class Cluster:
    """Encapsulates code points and glyphs composing a grapheme."""
    
    def __init__(self, codepoints: List[int], glyphs: List[aspose.words.shaping.Glyph]):
        """Initializes new instance of this class.
        
        :param codepoints: Array of Unicode points composing a grapheme.
        :param glyphs: Array of :class:`Glyph`\> composing a grapheme."""
        ...
    
    @overload
    @staticmethod
    def get_string(clusters: List[aspose.words.shaping.Cluster]) -> str:
        """Creates string using codepoints from the specified clusters."""
        ...
    
    @overload
    def get_string(self) -> str:
        """Creates string using codepoints from this cluster."""
        ...
    
    def get_width(self, em: int, font_size: float) -> float:
        """Returns width of the cluster."""
        ...
    
    def deep_clone(self) -> aspose.words.shaping.Cluster:
        """Returns a deep clone of this instance."""
        ...
    
    @property
    def codepoints(self) -> List[int]:
        """Gets codepoints of the cluster."""
        ...
    
    @property
    def codepoints_length(self) -> int:
        """Gets total number of codepoints in the :class:`Cluster`."""
        ...
    
    @property
    def glyphs(self) -> List[aspose.words.shaping.Glyph]:
        """Gets glyphs of the cluster."""
        ...
    
    ...

class Glyph:
    """Represents a glyph"""
    
    def __init__(self, glyph_index: int, advance: int, advance_offset: int, ascender_offset: int):
        """Initializes new instance of this class.
        
        :param glyph_index: Glyph index.
        :param advance: Advance metric of the glyph.
        :param advance_offset: Horizontal (x) offset.
        :param ascender_offset: Vertical (y) offset."""
        ...
    
    def get_width(self, em: int, font_size: float) -> float:
        """Returns width (advance) of the glyph in points."""
        ...
    
    def clone(self) -> aspose.words.shaping.Glyph:
        """Returns a clone of this instance."""
        ...
    
    @property
    def glyph_index(self) -> int:
        """Index of the glyph (GID) in the physical font."""
        ...
    
    @property
    def advance(self) -> int:
        """Advance width indicating placement for the subsequent glyph."""
        ...
    
    @advance.setter
    def advance(self, value: int):
        ...
    
    @property
    def advance_offset(self) -> int:
        """Horizontal (x) offset relative to glyph position.
        Mostly used to attach marks (like diacritics) to base characters."""
        ...
    
    @property
    def ascender_offset(self) -> int:
        """Vertical (y) offset relative to glyph position.
        Mostly used to attach marks (like diacritics) to base characters."""
        ...
    
    ...

class ITextShaper:
    """Provides methods for text shaping."""
    
    def shape_text(self, runs: List[str], direction: aspose.words.shaping.Direction, script: aspose.words.shaping.UnicodeScript, enabled_font_features: List[aspose.words.shaping.FontFeature], variations: List[aspose.words.shaping.VariationAxisCoordinate]) -> List[List[aspose.words.shaping.Cluster]]:
        """Returns :class:`Cluster` objects generated from a sequence of text fragments.
        Length of the returned array is equal to length of *runs*.
        If run at an index has corresponding clusters then result at the same index will have them recorded.
        
        :param runs: A sequence of text fragments
        :param direction: A direction of text
        :param script: A script
        :param enabled_font_features: A set of explicitly enabled OpenType features to consider
        :param variations: Font's variation axis values"""
        ...
    
    ...

class ITextShaperFactory:
    """An interface of a factory for constructing :class:`ITextShaper` implementations."""
    
    @overload
    def get_text_shaper(self, font_path: str, face_index: int) -> aspose.words.shaping.ITextShaper:
        """Returns new instance of a text shaper for the font specified by *fontPath* and*faceIndex*.
        
        :param font_path: An absolute path to the font file.
        :param face_index: An index of the font face in the TrueType font collection,
                           or 0 if specified font file is not TrueType font collection."""
        ...
    
    @overload
    def get_text_shaper(self, font_id: str, font_blob: bytes, face_index: int) -> aspose.words.shaping.ITextShaper:
        """Returns new instance of a text shaper for the font represented by *fontBlob* and*faceIndex*.
        
        :param font_id: A unique identifier that can be uniquely associated with the provided font *fontBlob*.
        :param font_blob: Byte array with the font data.
        :param face_index: An index of the font face in the TrueType font collection,
                           or 0 if *fontBlob* is not TrueType font collection."""
        ...
    
    ...

class VariationAxisCoordinate:
    """Represents an axis coordinate."""
    
    def __init__(self):
        ...
    
    @property
    def axis(self) -> aspose.words.shaping.VariationAxis:
        """Axis."""
        ...
    
    @axis.setter
    def axis(self, value: aspose.words.shaping.VariationAxis):
        ...
    
    @property
    def coordinate(self) -> float:
        """Coordinate."""
        ...
    
    @coordinate.setter
    def coordinate(self, value: float):
        ...
    
    ...

class Direction(Enum):
    """Text direction."""
    
    """Default value, same as :attr:`Direction.LTR`."""
    DEFAULT: int
    
    """Left-to-right writing direction."""
    LTR: int
    
    """Right-to-left writing direction."""
    RTL: int
    
    """Top-to-bottom writing direction."""
    TTB: int
    
    """Bottom-to-top writing direction."""
    BTT: int
    

class FontFeature(Enum):
    """Features provide information about how glyphs are used in a font to render a script.
    https://docs.microsoft.com/en-us/typography/opentype/spec/featuretags"""
    
    """To minimize the number of glyph alternates, it is sometimes desirable to decompose the default glyph for a character into two or more glyphs.
    Additionally, it may be preferable to compose default glyphs for two or more characters into a single glyph for better glyph processing.
    This feature permits such composition/decomposition.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_ae#ccmp
    Equivalent OpenType tag: 'ccmp'"""
    GLYPH_COMPOSITION_DECOMPOSITION: int
    
    """Replaces a sequence of glyphs with a single glyph which is preferred for typographic purposes.
    This feature covers the ligatures which the designer/manufacturer judges should be used in normal conditions.
    Equivalent OpenType tag: 'liga'
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_ko#liga"""
    STANDARD_LIGATURES: int
    
    """Replaces a sequence of glyphs with a single glyph which is preferred for typographic purposes.
    This feature covers those ligatures, which the script determines as required to be used in normal conditions.
    This feature is important for some scripts to ensure correct glyph formation.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_pt#rlig
    Equivalent OpenType tag: 'rlig'"""
    REQUIRED_LIGATURES: int
    
    """Replaces a sequence of glyphs with a single glyph which is preferred for typographic purposes.
    Unlike other ligature features, 'clig' specifies the context in which the ligature is recommended.
    This capability is important in some script designs and for swash ligatures.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_ae#clig
    Equivalent OpenType tag: 'clig'"""
    CONTEXTUAL_LIGATURES: int
    
    """Replaces a sequence of glyphs with a single glyph which is preferred for typographic purposes.
    This feature covers those ligatures which may be used for special effect, at the user’s preference.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_ae#dlig
    Equivalent OpenType tag: 'dlig'"""
    DISCRETIONARY_LIGATURES: int
    
    """Some ligatures were in common use in the past, but appear anachronistic today.
    Some fonts include the historical forms as alternates, so they can be used for a "period" effect.
    This feature replaces the default (current) forms with the historical alternates.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_fj#hlig
    Equivalent OpenType tag: 'hlig'"""
    HISTORICAL_LIGATURES: int
    
    """Replaces figure glyphs set on uniform (tabular) widths with corresponding glyphs set on glyph-specific (proportional) widths.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_pt#tag-pnum
    Equivalent OpenType tag: 'pnum'"""
    PROPORTIONAL_FIGURES: int
    
    """Replaces figure glyphs set on proportional widths with corresponding glyphs set on uniform (tabular) widths.
    Tabular widths will generally be the default, but this cannot be safely assumed.
    Of course this feature would not be present in monospaced designs.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_pt#tag-tnum
    Equivalent OpenType tag: 'tnum'"""
    TABULAR_FIGURES: int
    
    """This feature changes selected non-lining figures to lining figures.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_ko#lnum
    Equivalent OpenType tag: 'lnum'"""
    LINING_FIGURES: int
    
    """This feature changes selected figures from the default or lining style to oldstyle form.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_ko#onum
    Equivalent OpenType tag: 'onum'"""
    OLDSTYLE_FIGURES: int
    
    """Transforms default glyphs into glyphs that are appropriate for upright presentation in vertical writing mode.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_uz#tag-vert
    Equivalent OpenType tag: 'vert'"""
    VERTICAL_ALTERNATES: int
    
    """Replaces some fixed-width (half-, third- or quarter-width) or proportional-width glyphs (mostly Latin or katakana)
    with forms suitable for vertical writing (that is, rotated 90 degrees clockwise).
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_uz#tag-vrt2
    Equivalent OpenType tag: 'vrt2'"""
    VERTICAL_ALTERNATES_AND_ROTATION: int
    
    """Stylistic Set 1
    In addition to, or instead of, stylistic alternatives of individual glyphs (see 'salt' feature),
    some fonts may contain sets of stylistic variant glyphs corresponding to portions of the character set, e.g. multiple variants for lowercase letters in a Latin font.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_pt#tag-ss01---ss20
    Equivalent OpenType tag: 'ss01'"""
    STYLISTIC_SET01: int
    
    """Stylistic Set 2
    Equivalent OpenType tag: 'ss02'"""
    STYLISTIC_SET02: int
    
    """Stylistic Set 3
    Equivalent OpenType tag: 'ss03'"""
    STYLISTIC_SET03: int
    
    """Stylistic Set 4
    Equivalent OpenType tag: 'ss04'"""
    STYLISTIC_SET04: int
    
    """Stylistic Set 5
    Equivalent OpenType tag: 'ss05'"""
    STYLISTIC_SET05: int
    
    """Stylistic Set 6
    Equivalent OpenType tag: 'ss06'"""
    STYLISTIC_SET06: int
    
    """Stylistic Set 7
    Equivalent OpenType tag: 'ss07'"""
    STYLISTIC_SET07: int
    
    """Stylistic Set 8
    Equivalent OpenType tag: 'ss08'"""
    STYLISTIC_SET08: int
    
    """Stylistic Set 9
    Equivalent OpenType tag: 'ss09'"""
    STYLISTIC_SET09: int
    
    """Stylistic Set 10
    Equivalent OpenType tag: 'ss10'"""
    STYLISTIC_SET10: int
    
    """Stylistic Set 11
    Equivalent OpenType tag: 'ss11'"""
    STYLISTIC_SET11: int
    
    """Stylistic Set 12
    Equivalent OpenType tag: 'ss12'"""
    STYLISTIC_SET12: int
    
    """Stylistic Set 13
    Equivalent OpenType tag: 'ss13'"""
    STYLISTIC_SET13: int
    
    """Stylistic Set 14
    Equivalent OpenType tag: 'ss14'"""
    STYLISTIC_SET14: int
    
    """Stylistic Set 15
    Equivalent OpenType tag: 'ss15'"""
    STYLISTIC_SET15: int
    
    """Stylistic Set 16
    Equivalent OpenType tag: 'ss16'"""
    STYLISTIC_SET16: int
    
    """Stylistic Set 17
    Equivalent OpenType tag: 'ss17'"""
    STYLISTIC_SET17: int
    
    """Stylistic Set 18
    Equivalent OpenType tag: 'ss18'"""
    STYLISTIC_SET18: int
    
    """Stylistic Set 19
    Equivalent OpenType tag: 'ss19'"""
    STYLISTIC_SET19: int
    
    """Stylistic Set 20
    Equivalent OpenType tag: 'ss20'"""
    STYLISTIC_SET20: int
    
    """Adjusts amount of space between glyphs, generally to provide optically consistent spacing between glyphs.
    Although a well-designed typeface has consistent inter-glyph spacing overall, some glyph combinations require adjustment for improved legibility.
    Besides standard adjustment in the horizontal direction, this feature can supply size-dependent kerning data via device tables,
    "cross-stream" kerning in the Y text direction, and adjustment of glyph placement independent of the advance adjustment.
    Note that this feature may apply to runs of more than two glyphs, and would not be used in monospaced fonts.
    Also note that this feature does not apply to text set vertically.
    https://docs.microsoft.com/en-us/typography/opentype/spec/features_ko#kern
    Equivalent OpenType tag: 'kern'"""
    KERNING: int
    

class ScriptShapingLevel(Enum):
    """Describes shaping levels required by a script."""
    
    """Script does not require shaping."""
    NONE: int
    
    """This is used when the level for the script is not specified.
    
    It should not happen."""
    UNKNOWN: int
    
    """Script requires minimum shaping support.
    
    It is not clear, what Minimum means.
    Minimum is set for some very popular scripts (Latin, Cyrillic...)."""
    MINIMUM: int
    
    """Script requires full shaping support."""
    FULL: int
    

class UnicodeScript(Enum):
    """Unicode Character Database property: Script (sc).
    
    http://www.unicode.org/reports/tr24/tr24-29.html
    https://www.unicode.org/iso15924/
    http://goo.gl/x9ilM"""
    
    """Adlam script."""
    ADLAM: int
    
    """Caucasian_Albanian script."""
    CAUCASIAN_ALBANIAN: int
    
    """Ahom script."""
    AHOM: int
    
    """Arabic script."""
    ARABIC: int
    
    """Imperial_Aramaic script."""
    IMPERIAL_ARAMAIC: int
    
    """Armenian script."""
    ARMENIAN: int
    
    """Avestan script."""
    AVESTAN: int
    
    """Balinese script."""
    BALINESE: int
    
    """Bamum script."""
    BAMUM: int
    
    """Bassa_Vah script."""
    BASSA_VAH: int
    
    """Batak script."""
    BATAK: int
    
    """Bengali script."""
    BENGALI: int
    
    """Bhaiksuki script."""
    BHAIKSUKI: int
    
    """Bopomofo script."""
    BOPOMOFO: int
    
    """Brahmi script."""
    BRAHMI: int
    
    """Braille script."""
    BRAILLE: int
    
    """Buginese script."""
    BUGINESE: int
    
    """Buhid script."""
    BUHID: int
    
    """Chakma script."""
    CHAKMA: int
    
    """Canadian_Aboriginal script."""
    CANADIAN_ABORIGINAL: int
    
    """Carian script."""
    CARIAN: int
    
    """Cham script."""
    CHAM: int
    
    """Cherokee script."""
    CHEROKEE: int
    
    """Chorasmian script."""
    CHORASMIAN: int
    
    """Coptic script."""
    COPTIC: int
    
    """Cypriot script."""
    CYPRIOT: int
    
    """Cyrillic script."""
    CYRILLIC: int
    
    """Devanagari script."""
    DEVANAGARI: int
    
    """Dives_Akuru script."""
    DIVES_AKURU: int
    
    """Dogra script."""
    DOGRA: int
    
    """Deseret script."""
    DESERET: int
    
    """Duployan script."""
    DUPLOYAN: int
    
    """Egyptian_Hieroglyphs script."""
    EGYPTIAN_HIEROGLYPHS: int
    
    """Elbasan script."""
    ELBASAN: int
    
    """Elymaic script."""
    ELYMAIC: int
    
    """Ethiopic script."""
    ETHIOPIC: int
    
    """Georgian script."""
    GEORGIAN: int
    
    """Glagolitic script."""
    GLAGOLITIC: int
    
    """Gunjala_Gondi script."""
    GUNJALA_GONDI: int
    
    """Masaram_Gondi script."""
    MASARAM_GONDI: int
    
    """Gothic script."""
    GOTHIC: int
    
    """Grantha script."""
    GRANTHA: int
    
    """Greek script."""
    GREEK: int
    
    """Gujarati script."""
    GUJARATI: int
    
    """Gurmukhi script."""
    GURMUKHI: int
    
    """Hangul script."""
    HANGUL: int
    
    """Han script."""
    HAN: int
    
    """Hanunoo script."""
    HANUNOO: int
    
    """Hatran script."""
    HATRAN: int
    
    """Hebrew script."""
    HEBREW: int
    
    """Hiragana script."""
    HIRAGANA: int
    
    """Anatolian_Hieroglyphs script."""
    ANATOLIAN_HIEROGLYPHS: int
    
    """Pahawh_Hmong script."""
    PAHAWH_HMONG: int
    
    """Nyiakeng_Puachue_Hmong script."""
    NYIAKENG_PUACHUE_HMONG: int
    
    """Katakana_Or_Hiragana script."""
    KATAKANA_OR_HIRAGANA: int
    
    """Old_Hungarian script."""
    OLD_HUNGARIAN: int
    
    """Old_Italic script."""
    OLD_ITALIC: int
    
    """Javanese script."""
    JAVANESE: int
    
    """Kayah_Li script."""
    KAYAH_LI: int
    
    """Katakana script."""
    KATAKANA: int
    
    """Kharoshthi script."""
    KHAROSHTHI: int
    
    """Khmer script."""
    KHMER: int
    
    """Khojki script."""
    KHOJKI: int
    
    """Khitan_Small_Script script."""
    KHITAN_SMALL_SCRIPT: int
    
    """Kannada script."""
    KANNADA: int
    
    """Kaithi script."""
    KAITHI: int
    
    """Tai_Tham script."""
    TAI_THAM: int
    
    """Lao script."""
    LAO: int
    
    """Latin script."""
    LATIN: int
    
    """Lepcha script."""
    LEPCHA: int
    
    """Limbu script."""
    LIMBU: int
    
    """Linear_A script."""
    LINEAR_A: int
    
    """Linear_B script."""
    LINEAR_B: int
    
    """Lisu script."""
    LISU: int
    
    """Lycian script."""
    LYCIAN: int
    
    """Lydian script."""
    LYDIAN: int
    
    """Mahajani script."""
    MAHAJANI: int
    
    """Makasar script."""
    MAKASAR: int
    
    """Mandaic script."""
    MANDAIC: int
    
    """Manichaean script."""
    MANICHAEAN: int
    
    """Marchen script."""
    MARCHEN: int
    
    """Medefaidrin script."""
    MEDEFAIDRIN: int
    
    """Mende_Kikakui script."""
    MENDE_KIKAKUI: int
    
    """Meroitic_Cursive script."""
    MEROITIC_CURSIVE: int
    
    """Meroitic_Hieroglyphs script."""
    MEROITIC_HIEROGLYPHS: int
    
    """Malayalam script."""
    MALAYALAM: int
    
    """Modi script."""
    MODI: int
    
    """Mongolian script."""
    MONGOLIAN: int
    
    """Mro script."""
    MRO: int
    
    """Meetei_Mayek script."""
    MEETEI_MAYEK: int
    
    """Multani script."""
    MULTANI: int
    
    """Myanmar script."""
    MYANMAR: int
    
    """Nandinagari script."""
    NANDINAGARI: int
    
    """Old_North_Arabian script."""
    OLD_NORTH_ARABIAN: int
    
    """Nabataean script."""
    NABATAEAN: int
    
    """Newa script."""
    NEWA: int
    
    """Nko script."""
    NKO: int
    
    """Nushu script."""
    NUSHU: int
    
    """Ogham script."""
    OGHAM: int
    
    """Ol_Chiki script."""
    OL_CHIKI: int
    
    """Old_Turkic script."""
    OLD_TURKIC: int
    
    """Oriya script."""
    ORIYA: int
    
    """Osage script."""
    OSAGE: int
    
    """Osmanya script."""
    OSMANYA: int
    
    """Palmyrene script."""
    PALMYRENE: int
    
    """Pau_Cin_Hau script."""
    PAU_CIN_HAU: int
    
    """Old_Permic script."""
    OLD_PERMIC: int
    
    """Phags_Pa script."""
    PHAGS_PA: int
    
    """Inscriptional_Pahlavi script."""
    INSCRIPTIONAL_PAHLAVI: int
    
    """Psalter_Pahlavi script."""
    PSALTER_PAHLAVI: int
    
    """Phoenician script."""
    PHOENICIAN: int
    
    """Miao script."""
    MIAO: int
    
    """Inscriptional_Parthian script."""
    INSCRIPTIONAL_PARTHIAN: int
    
    """Rejang script."""
    REJANG: int
    
    """Hanifi_Rohingya script."""
    HANIFI_ROHINGYA: int
    
    """Runic script."""
    RUNIC: int
    
    """Samaritan script."""
    SAMARITAN: int
    
    """Old_South_Arabian script."""
    OLD_SOUTH_ARABIAN: int
    
    """Saurashtra script."""
    SAURASHTRA: int
    
    """SignWriting script."""
    SIGN_WRITING: int
    
    """Shavian script."""
    SHAVIAN: int
    
    """Sharada script."""
    SHARADA: int
    
    """Siddham script."""
    SIDDHAM: int
    
    """Khudawadi script."""
    KHUDAWADI: int
    
    """Sinhala script."""
    SINHALA: int
    
    """Sogdian script."""
    SOGDIAN: int
    
    """Old_Sogdian script."""
    OLD_SOGDIAN: int
    
    """Sora_Sompeng script."""
    SORA_SOMPENG: int
    
    """Soyombo script."""
    SOYOMBO: int
    
    """Sundanese script."""
    SUNDANESE: int
    
    """Syloti_Nagri script."""
    SYLOTI_NAGRI: int
    
    """Syriac script."""
    SYRIAC: int
    
    """Tagbanwa script."""
    TAGBANWA: int
    
    """Takri script."""
    TAKRI: int
    
    """Tai_Le script."""
    TAI_LE: int
    
    """New_Tai_Lue script."""
    NEW_TAI_LUE: int
    
    """Tamil script."""
    TAMIL: int
    
    """Tangut script."""
    TANGUT: int
    
    """Tai_Viet script."""
    TAI_VIET: int
    
    """Telugu script."""
    TELUGU: int
    
    """Tifinagh script."""
    TIFINAGH: int
    
    """Tagalog script."""
    TAGALOG: int
    
    """Thaana script."""
    THAANA: int
    
    """Thai script."""
    THAI: int
    
    """Tibetan script."""
    TIBETAN: int
    
    """Tirhuta script."""
    TIRHUTA: int
    
    """Ugaritic script."""
    UGARITIC: int
    
    """Vai script."""
    VAI: int
    
    """Warang_Citi script."""
    WARANG_CITI: int
    
    """Wancho script."""
    WANCHO: int
    
    """Old_Persian script."""
    OLD_PERSIAN: int
    
    """Cuneiform script."""
    CUNEIFORM: int
    
    """Yezidi script."""
    YEZIDI: int
    
    """Yi script."""
    YI: int
    
    """Zanabazar_Square script."""
    ZANABAZAR_SQUARE: int
    
    """Inherited script."""
    INHERITED: int
    
    """Common script."""
    COMMON: int
    
    """Unknown script."""
    UNKNOWN: int
    

class VariationAxis(Enum):
    """Represents OpenType Design-Variation Axis Tag.
    https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg"""
    
    """Registered tag for the roman/italic axis."""
    ITALIC: int
    
    """Registered tag for the optical-size axis.
    Note: The optical-size axis supersedes the OpenType `size` feature."""
    OPTICAL_SIZE: int
    
    """Registered tag for the slant axis."""
    SLANT: int
    
    """Registered tag for the weight axis."""
    WEIGHT: int
    
    """Registered tag for the width axis."""
    WIDTH: int
    

