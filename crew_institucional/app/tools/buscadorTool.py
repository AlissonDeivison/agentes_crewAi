from dotenv import load_dotenv
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

load_dotenv()

pesquisaTool = SerperDevTool()
scrapeTool = ScrapeWebsiteTool(
    follow_links=True,
    max_depth=8,
    max_links=20,
    allowed_domains=["unifacisa.edu.br"],
    block_pdf=True,
    allowed_tags=["h1", "h2", "p", "div", "span"],
)
