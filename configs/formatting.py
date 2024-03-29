from dataclasses import dataclass

from configs.config import PARSE_MODE


@dataclass
class Formatting:
    b: str  # noqa: VNE001
    i: str  # noqa: VNE001
    u: str  # noqa: VNE001
    s: str  # noqa: VNE001
    c: str  # noqa: VNE001
    cm: str
    # bold: str
    # ebold: str
    # italic: str
    # eitalic: str
    # strike: str
    # estrike: str
    # blockquotes: str
    # h1: str
    # eh1: str
    # h2: str
    # eh2: str
    # h3: str
    # eh3: str
    # h4: str
    # eh4: str
    # h5: str
    # eh5: str
    # h6: str
    # eh6: str


if PARSE_MODE == 'MARKDOWN':
    frm = Formatting(
                    b='*',
                    i='_',
                    u='__',
                    s='~',
                    c='`',
                    cm='```'
                    # bold='**',
                    # ebold='**',
                    # italic='*',
                    # eitalic='*',
                    # underline='',
                    # eunderline='',
                    # strike='<s>',
                    # estrike='</s>',
                    # blockquotes='>',
                    # h1='#',
                    # eh1='#',
                    # h2='##',
                    # eh2='##',
                    # h3='###',
                    # eh3='###',
                    # h4='####',
                    # eh4='####',
                    # h5='#####',
                    # eh5='#####',
                    # h6='######',
                    # eh6='######',
                    )
