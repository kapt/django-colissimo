# -*- coding: utf-8 -*-

from django.db import models
import types


ISO_3166_1_A3_TO_COUNTRYNAME = {
	"GBR":u"United kingdom of great britain and northern ireland",
	"AFG":u"Afghanistan",
	"ALA":u"Åland islands",
	"ALB":u"Albania",
	"DZA":u"Algeria",
	"ASM":u"American samoa",
	"AND":u"Andorra",
	"AGO":u"Angola",
	"AIA":u"Anguilla",
	"ATA":u"Antarctica",
	"ATG":u"Antigua and barbuda",
	"ARG":u"Argentina",
	"ARM":u"Armenia",
	"ABW":u"Aruba",
	"AUS":u"Australia",
	"AUT":u"Austria",
	"AZE":u"Azerbaijan",
	"BHS":u"Bahamas",
	"BHR":u"Bahrain",
	"BGD":u"Bangladesh",
	"BRB":u"Barbados",
	"BLR":u"Belarus",
	"BEL":u"Belgium",
	"BLZ":u"Belize",
	"BEN":u"Benin",
	"BMU":u"Bermuda",
	"BTN":u"Bhutan",
	"BOL":u"Bolivia",
	"BIH":u"Bosnia and herzegovina",
	"BWA":u"Botswana",
	"BVT":u"Bouvet island",
	"BRA":u"Brazil",
	"IOT":u"British indian ocean territory",
	"BRN":u"Brunei darussalam",
	"BGR":u"Bulgaria",
	"BFA":u"Burkina faso",
	"BDI":u"Burundi",
	"KHM":u"Cambodia",
	"CMR":u"Cameroon",
	"CAN":u"Canada",
	"CPV":u"Cape verde",
	"CYM":u"Cayman islands",
	"CAF":u"Central african republic",
	"TCD":u"Chad",
	"CHL":u"Chile",
	"CHN":u"China",
	"CXR":u"Christmas island",
	"CCK":u"Cocos (keeling) islands",
	"COL":u"Colombia",
	"COM":u"Comoros",
	"COG":u"Congo",
	"COD":u"Democratic republic of the congo",
	"COK":u"Cook islands",
	"CRI":u"Costa rica",
	"CIV":u"Côte d'ivoire",
	"HRV":u"Croatia",
	"CUB":u"Cuba",
	"CYP":u"Cyprus",
	"CZE":u"Czech republic",
	"DNK":u"Denmark",
	"DJI":u"Djibouti",
	"DMA":u"Dominica",
	"DOM":u"Dominican republic",
	"ECU":u"Ecuador",
	"EGY":u"Egypt",
	"SLV":u"El salvador",
	"GNQ":u"Equatorial guinea",
	"ERI":u"Eritrea",
	"EST":u"Estonia",
	"ETH":u"Ethiopia",
	"FLK":u"Falkland islands (malvinas)",
	"FRO":u"Faeroe islands",
	"FJI":u"Fiji",
	"FIN":u"Finland",
	"FRA":u"France",
	"GUF":u"French guiana",
	"PYF":u"French polynesia",
	"ATF":u"French southern territories",
	"GAB":u"Gabon",
	"GMB":u"Gambia",
	"GEO":u"Georgia",
	"DEU":u"Germany",
	"GHA":u"Ghana",
	"GIB":u"Gibraltar",
	"GRC":u"Greece",
	"GRL":u"Greenland",
	"GRD":u"Grenada",
	"GLP":u"Guadeloupe",
	"GUM":u"Guam",
	"GTM":u"Guatemala",
	"GGY":u"Guernsey",
	"GIN":u"Guinea",
	"GNB":u"Guinea-bissau",
	"GUY":u"Guyana",
	"HTI":u"Haiti",
	"HMD":u"Heard island and mcdonald islands",
	"VAT":u"Holy see",
	"HND":u"Honduras",
	"HKG":u"Hong kong special administrative region of china",
	"HUN":u"Hungary",
	"ISL":u"Iceland",
	"IND":u"India",
	"IDN":u"Indonesia",
	"IRN":u"Iran, islamic republic of",
	"IRQ":u"Iraq",
	"IRL":u"Ireland",
	"IMN":u"Isle of man",
	"ISR":u"Israel",
	"ITA":u"Italy",
	"JAM":u"Jamaica",
	"JPN":u"Japan",
	"JEY":u"Jersey",
	"JOR":u"Jordan",
	"KAZ":u"Kazakhstan",
	"KEN":u"Kenya",
	"KIR":u"Kiribati",
	"PRK":u"Democratic people's republic of korea",
	"KOR":u"Republic of korea",
	"KWT":u"Kuwait",
	"KGZ":u"Kyrgyzstan",
	"LAO":u"Lao people's democratic republic",
	"LVA":u"Latvia",
	"LBN":u"Lebanon",
	"LSO":u"Lesotho",
	"LBR":u"Liberia",
	"LBY":u"Libyan arab jamahiriya",
	"LIE":u"Liechtenstein",
	"LTU":u"Lithuania",
	"LUX":u"Luxembourg",
	"MAC":u"Macao special administrative region of china",
	"MKD":u"The former yugoslav republic of macedonia",
	"MDG":u"Madagascar",
	"MWI":u"Malawi",
	"MYS":u"Malaysia",
	"MDV":u"Maldives",
	"MLI":u"Mali",
	"MLT":u"Malta",
	"MHL":u"Marshall islands",
	"MTQ":u"Martinique",
	"MRT":u"Mauritania",
	"MUS":u"Mauritius",
	"MYT":u"Mayotte",
	"MEX":u"Mexico",
	"FSM":u"Micronesia, federated states of",
	"MDA":u"Republic of moldova",
	"MCO":u"Monaco",
	"MNG":u"Mongolia",
	"MNE":u"Montenegro",
	"MSR":u"Montserrat",
	"MAR":u"Morocco",
	"MOZ":u"Mozambique",
	"MMR":u"Myanmar",
	"NAM":u"Namibia",
	"NRU":u"Nauru",
	"NPL":u"Nepal",
	"NLD":u"Netherlands",
	"ANT":u"Netherlands antilles",
	"NCL":u"New caledonia",
	"NZL":u"New zealand",
	"NIC":u"Nicaragua",
	"NER":u"Niger",
	"NGA":u"Nigeria",
	"NIU":u"Niue",
	"NFK":u"Norfolk island",
	"MNP":u"Northern mariana islands",
	"NOR":u"Norway",
	"OMN":u"Oman",
	"PAK":u"Pakistan",
	"PLW":u"Palau",
	"PSE":u"Occupied palestinian territory",
	"PAN":u"Panama",
	"PNG":u"Papua new guinea",
	"PRY":u"Paraguay",
	"PER":u"Peru",
	"PHL":u"Philippines",
	"PCN":u"Pitcairn",
	"POL":u"Poland",
	"PRT":u"Portugal",
	"PRI":u"Puerto rico",
	"QAT":u"Qatar",
	"REU":u"Réunion",
	"ROU":u"Romania",
	"RUS":u"Russian federation",
	"RWA":u"Rwanda",
	"SHN":u"Saint helena",
	"KNA":u"Saint kitts and nevis",
	"LCA":u"Saint lucia",
	"SPM":u"Saint pierre and miquelon",
	"VCT":u"Saint vincent and the grenadines",
	"WSM":u"Samoa",
	"SMR":u"San marino",
	"STP":u"Sao tome and principe",
	"SAU":u"Saudi arabia",
	"SEN":u"Senegal",
	"SRB":u"Serbia",
	"SYC":u"Seychelles",
	"SLE":u"Sierra leone",
	"SGP":u"Singapore",
	"SVK":u"Slovakia",
	"SVN":u"Slovenia",
	"SLB":u"Solomon islands",
	"SOM":u"Somalia",
	"ZAF":u"South africa",
	"SGS":u"South georgia and the south sandwich islands",
	"ESP":u"Spain",
	"LKA":u"Sri lanka",
	"SDN":u"Sudan",
	"SUR":u"Suriname",
	"SJM":u"Svalbard and jan mayen islands",
	"SWZ":u"Swaziland",
	"SWE":u"Sweden",
	"CHE":u"Switzerland",
	"SYR":u"Syrian arab republic",
	"TWN":u"Taiwan, province of china",
	"TJK":u"Tajikistan",
	"THA":u"Thailand",
	"TLS":u"Timor-leste",
	"TGO":u"Togo",
	"TKL":u"Tokelau",
	"TON":u"Tonga",
	"TTO":u"Trinidad and tobago",
	"TUN":u"Tunisia",
	"TUR":u"Turkey",
	"TKM":u"Turkmenistan",
	"TCA":u"Turks and caicos islands",
	"TUV":u"Tuvalu",
	"UGA":u"Uganda",
	"UKR":u"Ukraine",
	"URY":u"Uruguay",
	"UZB":u"Uzbekistan",
	"VUT":u"Vanuatu",
	"VEN":u"Venezuela (bolivarian republic of)",
	"VNM":u"Viet nam",
	"VGB":u"British virgin islands",
	"VIR":u"United states virgin islands",
	"WLF":u"Wallis and futuna islands",
	"ESH":u"Western sahara",
	"YEM":u"Yemen",
	"ZMB":u"Zambia",
	"ZWE":u"Zimbabwe",
	"ARE":u'United Arab Emirates',
	"TZA":u'United Republic of Tanzania',
	"USA":u'United States of America',
	"UMI":u'United States Minor Outlying Islands',
}


class Region(models.Model):
	name = models.CharField(max_length=255)

	# France
	FMA = (u'France', u'Monaco', u'Andorra')
	# Outre-mer OM1
	OM1 = (u'Guadeloupe', u'Martinique', u'French Guiana', u'Réunion', u'Mayotte',
		   u'Saint Pierre and Miquelon', u'Saint Martin', u'Saint Barthélémy')
	# Outre-mer OM2
	OM2 = (u'New Caledonia', u'French Polynesia', u'Wallis and Futuna Islands',
		   u'French Southern Territories')
	# International Zone A
	IZA = (u'Switzerland', u'Norway', u'Austria', u'Belgium', u'Bulgaria', u'Cyprus',
		   u'Czech Republic', u'Denmark', u'Estonia', u'Finland', u'Germany',
		   u'Greece', u'Hungary', u'Italy', u'Latvia', u'Lithuania', u'Luxembourg',
		   u'Malta', u'Netherlands', u'Poland', u'Portugal', u'Ireland', u'Romania',
		   u'Slovakia', u'Slovenia', u'Spain', u'Sweden',
		   u'United Kingdom of Great Britain and Northern Ireland', u'Gibraltar',
		   u'Guernsey', u'Jersey', u'Liechtenstein', u'Norway', u'San Marino')
	# International Zone B
	IZB = (u'Morocco', u'Algeria', u'Tunisia', u'Libyan Arab Jamahiriya',
		   u'Mauritania', u'Western Sahara', u'Albania', u'Armenia', u'Azerbaijan',
		   u'Ukraine', u'Belarus', u'Bosnia and Herzegovina', u'Croatia', u'Georgia',
		   u'Iceland', u'The former Yugoslav Republic of Macedonia',
		   u'Republic of Moldova', u'Russian Federation', u'Serbia', u'Turkey')
	# International Zone C
	IZC = (u'Afghanistan', u'Angola', u'Argentina', u'Zimbabwe', u'Zambia', u'Yemen',
		   u'Uganda', u'Bahrain', u'Chad', u'Benin', u'Botswana', u'Burkina Faso',
		   u'Burundi', u'Cameroon', u'Canada', u'Cape Verde',
		   u'Central African Republic', u'Comoros', u'Congo',
		   u'Democratic Republic of the Congo', u'Djibouti', u'Egypt',
		   u'Equatorial Guinea', u'Ethiopia', u'Gabon', u'Gambia', u'Ghana',
		   u'Guinea', u'Iran, Islamic Republic of', u'Iraq', u'Israel', u'Jordan',
		   u'Kenya', u'Kuwait', u'Lebanon', u'Lesotho', u'Liberia', u"Côte d'Ivoire",
		   u'Madagascar', u'Mali', u'Marshall Islands', u'Mozambique', u'Namibia',
		   u'Niger', u'Nigeria', u'Oman', u'Pakistan', u'Qatar', u'Rwanda',
		   u'Saudi Arabia', u'Senegal', u'South Africa', u'Sudan', u'Swaziland',
		   u'Syrian Arab Republic', u'United Republic of Tanzani', u'Timor-Leste',
		   u'Togo', u'United Arab Emirates', u'United States of America', u'United Republic of Tanzania',
		    )
	# International Zone D
	IZD = (u'American Samoa', u'Anguilla', u'Antarctica', u'Antigua and Barbuda',
		   u'Aruba', u'Australia', u'Bahamas', u'United States Virgin Islands',
		   u'British Virgin Islands', u'Viet Nam',
		   u'Venezuela (Bolivarian Republic of)', u'Vanuatu', u'Uzbekistan',
		   u'Uruguay', u'Tuvalu', u'Bangladesh', u'Barbados', u'China', u'Chile',
		   u'Belize', u'Bermuda', u'Bhutan', u'Bolivia', u'Bouvet Island', u'Brazil',
		   u'British Indian Ocean Territory', u'Brunei Darussalam', u'Cambodia',
		   u'Cayman Islands', u'Christmas Island', u'Cocos (Keeling) Islands',
		   u'Colombia', u'Cook Islands', u'Costa Rica', u'Cuba', u'Dominica',
		   u'Dominican Republic', u'Ecuador', u'El Salvador', u'Eritrea',
		   u'Falkland Islands (Malvinas)', u'Faeroe Islands', u'Fiji', u'Guyana',
		   u'Greenland', u'Grenada', u'Guam', u'Guatemala', u'Guinea-Bissau',
		   u'Haiti', u'Heard Island and Mcdonald Islands', u'Holy See', u'Honduras',
		   u'Hong Kong Special Administrative Region of China', u'India',
		   u'Indonesia', u'Isle of Man', u'Jamaica', u'Japan', u'Kazakhstan',
		   u'Kiribati', u'French Southern Territories', u'Republic of Korea',
		   u'Kyrgyzstan', u"Democratic People's Republic of Korea",
		   u"Lao People's Democratic Republic",
		   u'Macao Special Administrative Region of China', u'Malawi', u'Malaysia',
		   u'Maldives', u'Mauritius', u'Mexico', u'Micronesia, Federated States of',
		   u'Mongolia', u'Montenegro', u'Montserrat', u'Myanmar', u'Nauru', u'Nepal',
		   u'Netherlands Antilles', u'New Zealand', u'Nicaragua', u'Niue',
		   u'Norfolk Island', u'Northern Mariana Islands', u'Palau',
		   u'Occupied Palestinian Territory', u'Panama', u'Papua New Guinea',
		   u'Paraguay', u'Peru', u'Philippines', u'Pitcairn', u'Puerto Rico',
		   u'Saint Helena', u'Saint Kitts and Nevis', u'Saint Lucia',
		   u'Saint Vincent and the Grenadines', u'Samoa', u'Sao Tome and Principe',
		   u'Seychelles', u'Sierra Leone', u'Singapore', u'Solomon Islands',
		   u'Somalia', u'South Georgia and the South Sandwich Islands',
		   u'Sri Lanka', u'Suriname', u'Svalbard and Jan Mayen Islands',
		   u'Taiwan, Province of China', u'Tajikistan', u'Thailand', u'Tokelau',
		   u'Tonga', u'Trinidad and Tobago', u'Turkmenistan',
		   u'Turks and Caicos Islands', u'United States Minor Outlying Islands',
		   u'Åland Islands')

	_lookup = (u'France', u'OM1', u'OM2', u'Zone A', u'Zone B', u'Zone C', u'Zone D')

	@staticmethod
	def get_region_from_country(country):
		if type(country) != types.StringType and type(country) != types.UnicodeType:
			raise TypeError, u"Country must be a string, not %s" % type(country)
		cty = country.strip().lower()
		# France
		zones = (Region.FMA, Region.OM1, Region.OM2, Region.IZA, Region.IZB, Region.IZC, Region.IZD)
		for k in range(len(zones)):
			for z in zones[k]:
				if cty == z.strip().lower():
					return Region.objects.get(name__contains=Region._lookup[k])
		return None

	def __repr__(self):
		return u"<Region: %s>" % self.name

class Recommanded(models.Model):
	"""
	Recommanded
	"""
	level = models.CharField(max_length=3, unique=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.level

class Rate(models.Model):
	# Up to this weight (in kg)
	weight = models.DecimalField(max_digits=5, decimal_places=2)
	# Signature on delivery?
	signature = models.BooleanField(default=False)
	# Deposit proof?
	deposit = models.BooleanField(default=False)
	# Tracking number?
	tracking = models.BooleanField(default=False)
	# Rate in Euro
	price = models.DecimalField(max_digits=5, decimal_places=2)
	# FKs
	region = models.ForeignKey(Region)
	recommanded = models.ForeignKey(Recommanded)

	@staticmethod
	def get_rates(country_iso_code, weight):
		"""
		Example: lowest rate for a 4.2 kg box to France:
		         Rate.get_rates(u'France', 4.2).get(recommanded__level='R0')
		"""
		if type(country_iso_code) != types.StringType and type(country_iso_code) != types.UnicodeType:
			raise TypeError, u"Country must be a string, not %s" % type(country_iso_code)
		if type(weight) != types.FloatType and type(weight) != types.IntType:
			raise TypeError, u"Weight must be a float"
		if weight < 0 or weight > 30:
			raise ValueError, u"Colissimo only supports 0<weight<=30 kg"

		from decimal import Decimal
		country = ISO_3166_1_A3_TO_COUNTRYNAME[country_iso_code]
		r = Region.get_region_from_country(country)
		if r is None:
			raise ValueError, u"Bad country value '%s': could not determine region" % country

		# A very dirty way to retrieve the cheapest rate for each Recommanded.
		# I think it's not possible to make this in one request using mysql (maybe with postgre).
		rates_ids = []
		for recommanded in Recommanded.objects.all():
			rs = Rate.objects.filter(weight__gte=Decimal(str(weight)), region=r, recommanded=recommanded).order_by("price")[:1]
			if rs.exists():
				rates_ids.append(rs[0].id)

		return Rate.objects.filter(id__in=rates_ids).order_by(u'price')

	def __repr__(self):
		return u"<Rate: max %.2fkg@%s, %.2f EUR>" % (self.weight, self.recommanded, self.price)

	class Meta:
		unique_together = ((u'weight', 'region', 'recommanded'))

