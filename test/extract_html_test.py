from src.stages.extract.extract_html import ExtractHtml
from src.drivers.html_collector import HtmlCollector
from src.drivers.http_requester import HttpRequester
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

def test_extract():
    http_requester = HttpRequester('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
    html_collector = HtmlCollector()
    extract_html = ExtractHtml(http_requester, html_collector)

    response = extract_html.extract()

    assert isinstance(response, ExtractContract)

def test_extract_error():
    http_requester = 'generate error'
    html_collector = HtmlCollector()
    extract_html = ExtractHtml(http_requester, html_collector)

    try:
        extract_html.extract()
    except Exception as exception: # pylint: disable=broad-except
        assert isinstance(exception, ExtractError)
