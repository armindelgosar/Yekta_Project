from BaseAdvertising import BaseAdvertising
from Ad import Ad
from Advertiser import Advertiser

baseAdvertising = BaseAdvertising()
advertiser1 = Advertiser(1, "name1")
advertiser2 = Advertiser(2, "name2")
ad1 = Ad(1, "title1", "img-url1", "link1", advertiser1)
ad2 = Ad(2, "title2", "img-url2", "link2", advertiser2)
baseAdvertising.describe_me()
ad2.describeMe()
advertiser1.describe_me()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad1.inc_views()
ad2.inc_views()
ad1.inc_clicks()
ad1.inc_clicks()
ad2.inc_clicks()
advertiser2.get_name()
advertiser2.set_name("new name")
advertiser2.get_name()
ad1.get_clicks()
advertiser2.get_clicks()
Advertiser.getTotalClicks()
Advertiser.help()
