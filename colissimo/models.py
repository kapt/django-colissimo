# -*- coding: utf-8 -*-

from decimal import Decimal

from django.db import models


ISO_3166_1_A3_TO_COUNTRYNAME = {
    "GBR": "United kingdom of great britain and northern ireland",
    "AFG": "Afghanistan",
    "ALA": "Åland islands",
    "ALB": "Albania",
    "DZA": "Algeria",
    "ASM": "American samoa",
    "AND": "Andorra",
    "AGO": "Angola",
    "AIA": "Anguilla",
    "ATA": "Antarctica",
    "ATG": "Antigua and barbuda",
    "ARG": "Argentina",
    "ARM": "Armenia",
    "ABW": "Aruba",
    "AUS": "Australia",
    "AUT": "Austria",
    "AZE": "Azerbaijan",
    "BHS": "Bahamas",
    "BHR": "Bahrain",
    "BGD": "Bangladesh",
    "BRB": "Barbados",
    "BLR": "Belarus",
    "BEL": "Belgium",
    "BLZ": "Belize",
    "BEN": "Benin",
    "BMU": "Bermuda",
    "BTN": "Bhutan",
    "BOL": "Bolivia",
    "BIH": "Bosnia and herzegovina",
    "BWA": "Botswana",
    "BVT": "Bouvet island",
    "BRA": "Brazil",
    "IOT": "British indian ocean territory",
    "BRN": "Brunei darussalam",
    "BGR": "Bulgaria",
    "BFA": "Burkina faso",
    "BDI": "Burundi",
    "KHM": "Cambodia",
    "CMR": "Cameroon",
    "CAN": "Canada",
    "CPV": "Cape verde",
    "CYM": "Cayman islands",
    "CAF": "Central african republic",
    "TCD": "Chad",
    "CHL": "Chile",
    "CHN": "China",
    "CXR": "Christmas island",
    "CCK": "Cocos (keeling) islands",
    "COL": "Colombia",
    "COM": "Comoros",
    "COG": "Congo",
    "COD": "Democratic republic of the congo",
    "COK": "Cook islands",
    "CRI": "Costa rica",
    "CIV": "Côte d'ivoire",
    "HRV": "Croatia",
    "CUB": "Cuba",
    "CYP": "Cyprus",
    "CZE": "Czech republic",
    "DNK": "Denmark",
    "DJI": "Djibouti",
    "DMA": "Dominica",
    "DOM": "Dominican republic",
    "ECU": "Ecuador",
    "EGY": "Egypt",
    "SLV": "El salvador",
    "GNQ": "Equatorial guinea",
    "ERI": "Eritrea",
    "EST": "Estonia",
    "ETH": "Ethiopia",
    "FLK": "Falkland islands (malvinas)",
    "FRO": "Faeroe islands",
    "FJI": "Fiji",
    "FIN": "Finland",
    "FRA": "France",
    "GUF": "French guiana",
    "PYF": "French polynesia",
    "ATF": "French southern territories",
    "GAB": "Gabon",
    "GMB": "Gambia",
    "GEO": "Georgia",
    "DEU": "Germany",
    "GHA": "Ghana",
    "GIB": "Gibraltar",
    "GRC": "Greece",
    "GRL": "Greenland",
    "GRD": "Grenada",
    "GLP": "Guadeloupe",
    "GUM": "Guam",
    "GTM": "Guatemala",
    "GGY": "Guernsey",
    "GIN": "Guinea",
    "GNB": "Guinea-bissau",
    "GUY": "Guyana",
    "HTI": "Haiti",
    "HMD": "Heard island and mcdonald islands",
    "VAT": "Holy see",
    "HND": "Honduras",
    "HKG": "Hong kong special administrative region of china",
    "HUN": "Hungary",
    "ISL": "Iceland",
    "IND": "India",
    "IDN": "Indonesia",
    "IRN": "Iran, islamic republic of",
    "IRQ": "Iraq",
    "IRL": "Ireland",
    "IMN": "Isle of man",
    "ISR": "Israel",
    "ITA": "Italy",
    "JAM": "Jamaica",
    "JPN": "Japan",
    "JEY": "Jersey",
    "JOR": "Jordan",
    "KAZ": "Kazakhstan",
    "KEN": "Kenya",
    "KIR": "Kiribati",
    "PRK": "Democratic people's republic of korea",
    "KOR": "Republic of korea",
    "KWT": "Kuwait",
    "KGZ": "Kyrgyzstan",
    "LAO": "Lao people's democratic republic",
    "LVA": "Latvia",
    "LBN": "Lebanon",
    "LSO": "Lesotho",
    "LBR": "Liberia",
    "LBY": "Libyan arab jamahiriya",
    "LIE": "Liechtenstein",
    "LTU": "Lithuania",
    "LUX": "Luxembourg",
    "MAC": "Macao special administrative region of china",
    "MKD": "The former yugoslav republic of macedonia",
    "MDG": "Madagascar",
    "MWI": "Malawi",
    "MYS": "Malaysia",
    "MDV": "Maldives",
    "MLI": "Mali",
    "MLT": "Malta",
    "MHL": "Marshall islands",
    "MTQ": "Martinique",
    "MRT": "Mauritania",
    "MUS": "Mauritius",
    "MYT": "Mayotte",
    "MEX": "Mexico",
    "FSM": "Micronesia, federated states of",
    "MDA": "Republic of moldova",
    "MCO": "Monaco",
    "MNG": "Mongolia",
    "MNE": "Montenegro",
    "MSR": "Montserrat",
    "MAR": "Morocco",
    "MOZ": "Mozambique",
    "MMR": "Myanmar",
    "NAM": "Namibia",
    "NRU": "Nauru",
    "NPL": "Nepal",
    "NLD": "Netherlands",
    "ANT": "Netherlands antilles",
    "NCL": "New caledonia",
    "NZL": "New zealand",
    "NIC": "Nicaragua",
    "NER": "Niger",
    "NGA": "Nigeria",
    "NIU": "Niue",
    "NFK": "Norfolk island",
    "MNP": "Northern mariana islands",
    "NOR": "Norway",
    "OMN": "Oman",
    "PAK": "Pakistan",
    "PLW": "Palau",
    "PSE": "Occupied palestinian territory",
    "PAN": "Panama",
    "PNG": "Papua new guinea",
    "PRY": "Paraguay",
    "PER": "Peru",
    "PHL": "Philippines",
    "PCN": "Pitcairn",
    "POL": "Poland",
    "PRT": "Portugal",
    "PRI": "Puerto rico",
    "QAT": "Qatar",
    "REU": "Réunion",
    "ROU": "Romania",
    "RUS": "Russian federation",
    "RWA": "Rwanda",
    "SHN": "Saint helena",
    "KNA": "Saint kitts and nevis",
    "LCA": "Saint lucia",
    "SPM": "Saint pierre and miquelon",
    "VCT": "Saint vincent and the grenadines",
    "WSM": "Samoa",
    "SMR": "San marino",
    "STP": "Sao tome and principe",
    "SAU": "Saudi arabia",
    "SEN": "Senegal",
    "SRB": "Serbia",
    "SYC": "Seychelles",
    "SLE": "Sierra leone",
    "SGP": "Singapore",
    "SVK": "Slovakia",
    "SVN": "Slovenia",
    "SLB": "Solomon islands",
    "SOM": "Somalia",
    "ZAF": "South africa",
    "SGS": "South georgia and the south sandwich islands",
    "ESP": "Spain",
    "LKA": "Sri lanka",
    "SDN": "Sudan",
    "SUR": "Suriname",
    "SJM": "Svalbard and jan mayen islands",
    "SWZ": "Swaziland",
    "SWE": "Sweden",
    "CHE": "Switzerland",
    "SYR": "Syrian arab republic",
    "TWN": "Taiwan, province of china",
    "TJK": "Tajikistan",
    "THA": "Thailand",
    "TLS": "Timor-leste",
    "TGO": "Togo",
    "TKL": "Tokelau",
    "TON": "Tonga",
    "TTO": "Trinidad and tobago",
    "TUN": "Tunisia",
    "TUR": "Turkey",
    "TKM": "Turkmenistan",
    "TCA": "Turks and caicos islands",
    "TUV": "Tuvalu",
    "UGA": "Uganda",
    "UKR": "Ukraine",
    "URY": "Uruguay",
    "UZB": "Uzbekistan",
    "VUT": "Vanuatu",
    "VEN": "Venezuela (bolivarian republic of)",
    "VNM": "Viet nam",
    "VGB": "British virgin islands",
    "VIR": "United states virgin islands",
    "WLF": "Wallis and futuna islands",
    "ESH": "Western sahara",
    "YEM": "Yemen",
    "ZMB": "Zambia",
    "ZWE": "Zimbabwe",
    "ARE": 'United Arab Emirates',
    "TZA": 'United Republic of Tanzania',
    "USA": 'United States of America',
    "UMI": 'United States Minor Outlying Islands',
}


class Region(models.Model):
    name = models.CharField(max_length=255)

    # France
    FMA = ('France', 'Monaco', 'Andorra')

    # Outre-mer OM1
    OM1 = ('Guadeloupe', 'Martinique', 'French Guiana', 'Réunion', 'Mayotte',
           'Saint Pierre and Miquelon', 'Saint Martin', 'Saint Barthélémy')

    # Outre-mer OM2
    OM2 = ('New Caledonia', 'French Polynesia', 'Wallis and Futuna Islands',
           'French Southern Territories')

    # International Zone A
    IZA = ('Switzerland', 'Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus',
           'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'Germany',
           'Greece', 'Hungary', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg',
           'Malta', 'Netherlands', 'Poland', 'Portugal', 'Ireland', 'Romania',
           'Slovakia', 'Slovenia', 'Spain', 'Sweden',
           'United Kingdom of Great Britain and Northern Ireland', 'Liechtenstein', 'San Marino', 'Holy See')

    # International Zone B
    IZB = ('Norway', 'Morocco', 'Algeria', 'Tunisia',
           'Albania', 'Armenia', 'Azerbaijan',
           'Ukraine', 'Belarus', 'Bosnia and Herzegovina', 'Georgia',
           'Iceland', 'The former Yugoslav Republic of Macedonia',
           'Republic of Moldova', 'Serbia', 'Turkey', 'Montenegro')

    # International Zone C
    IZC = ('Afghanistan', 'Angola', 'Argentina', 'Zimbabwe', 'Zambia', 'Yemen',
           'Uganda', 'Bahrain', 'Chad', 'Benin', 'Botswana', 'Burkina Faso',
           'Burundi', 'Cameroon', 'Canada', 'Cape Verde',
           'Central African Republic', 'Comoros', 'Congo',
           'Democratic Republic of the Congo', 'Djibouti', 'Egypt',
           'Equatorial Guinea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Gibraltar',
           'Guinea', 'Iran, Islamic Republic of', 'Iraq', 'Israel', 'Jordan',
           'Kenya', 'Kuwait', 'Lebanon', 'Lesotho', 'Liberia', 'Libyan Arab Jamahiriya', "Côte d'Ivoire",
           'Madagascar', 'Mali', 'Marshall Islands', 'Mozambique', 'Namibia',
           'Niger', 'Nigeria', 'Oman', 'Pakistan', 'Qatar', 'Rwanda',
           'Saudi Arabia', 'Senegal', 'South Africa', 'Sudan', 'Swaziland',
           'Syrian Arab Republic', 'United Republic of Tanzani', 'Timor-Leste',
           'Togo', 'United Arab Emirates', 'United States of America', 'United Republic of Tanzania',
           'American Samoa', 'Anguilla', 'Antarctica', 'Antigua and Barbuda',
           'Aruba', 'Australia', 'Bahamas', 'United States Virgin Islands',
           'British Virgin Islands', 'Viet Nam',
           'Venezuela (Bolivarian Republic of)', 'Vanuatu', 'Uzbekistan',
           'Uruguay', 'Tuvalu', 'Bangladesh', 'Barbados', 'China', 'Chile',
           'Belize', 'Bermuda', 'Bhutan', 'Bolivia', 'Bouvet Island', 'Brazil',
           'British Indian Ocean Territory', 'Brunei Darussalam', 'Cambodia',
           'Cayman Islands', 'Christmas Island', 'Cocos (Keeling) Islands',
           'Colombia', 'Cook Islands', 'Costa Rica', 'Cuba', 'Dominica',
           'Dominican Republic', 'Ecuador', 'El Salvador', 'Eritrea',
           'Falkland Islands (Malvinas)', 'Faeroe Islands', 'Fiji', 'Guyana',
           'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guinea-Bissau',
           'Haiti', 'Heard Island and Mcdonald Islands', 'Honduras',
           'Hong Kong Special Administrative Region of China', 'India',
           'Indonesia', 'Isle of Man', 'Jamaica', 'Japan', 'Kazakhstan',
           'Kiribati', 'French Southern Territories', 'Republic of Korea',
           'Kyrgyzstan', "Democratic People's Republic of Korea",
           "Lao People's Democratic Republic",
           'Macao Special Administrative Region of China', 'Malawi', 'Malaysia',
           'Maldives', 'Mauritius', 'Mauritania', 'Mexico', 'Micronesia, Federated States of',
           'Mongolia', 'Montserrat', 'Myanmar', 'Nauru', 'Nepal',
           'Netherlands Antilles', 'New Zealand', 'Nicaragua', 'Niue',
           'Norfolk Island', 'Northern Mariana Islands', 'Palau',
           'Occupied Palestinian Territory', 'Panama', 'Papua New Guinea',
           'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Puerto Rico', 'Russian Federation',
           'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia',
           'Saint Vincent and the Grenadines', 'Samoa', 'Sao Tome and Principe',
           'Seychelles', 'Sierra Leone', 'Singapore', 'Solomon Islands',
           'Somalia', 'South Georgia and the South Sandwich Islands',
           'Sri Lanka', 'Suriname', 'Svalbard and Jan Mayen Islands',
           'Taiwan, Province of China', 'Tajikistan', 'Thailand', 'Tokelau',
           'Tonga', 'Trinidad and Tobago', 'Turkmenistan',
           'Turks and Caicos Islands', 'United States Minor Outlying Islands',
           'Åland Islands', 'Guernsey', 'Jersey', 'Western Sahara',)

    _lookup = ('France', 'OM1', 'OM2', 'Zone A', 'Zone B', 'Zone C',)

    @staticmethod
    def get_region_from_country(country):
        if not isinstance(country, str):
            raise TypeError("Country must be a string, not %s" % type(country))

        cty = country.strip().lower()

        # France
        zones = (Region.FMA, Region.OM1, Region.OM2, Region.IZA, Region.IZB, Region.IZC,)
        for k in range(len(zones)):
            for z in zones[k]:
                if cty == z.strip().lower():
                    return Region.objects.get(name__contains=Region._lookup[k])
        return None

    def __str__(self):
        return "<Region: %s>" % self.name


class Recommanded(models.Model):
    """
    Recommanded
    """
    level = models.CharField(max_length=4, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

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
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    recommanded = models.ForeignKey(Recommanded, on_delete=models.CASCADE)

    @staticmethod
    def get_rates(country_iso_code, weight):
        """
        Example: lowest rate for a 4.2 kg box to France:
                 Rate.get_rates(u'France', 4.2).get(recommanded__level='R0')
        """
        if not isinstance(country_iso_code, str):
            raise TypeError("Country must be a string, not %s" % type(country_iso_code))

        if not isinstance(weight, float) and not isinstance(weight, int) and not isinstance(weight, Decimal):
            raise TypeError("Weight must be a float")

        if weight < 0 or weight > 30:
            raise ValueError("Colissimo only supports 0<weight<=30 kg")

        country = ISO_3166_1_A3_TO_COUNTRYNAME[country_iso_code]
        r = Region.get_region_from_country(country)
        if r is None:
            raise ValueError("Bad country value '%s': could not determine region" % country)

        # A very dirty way to retrieve the cheapest rate for each Recommanded.
        # I think it's not possible to make this in one request using mysql (maybe with postgre).
        rates_ids = []
        for recommanded in Recommanded.objects.all():
            rs = Rate.objects.filter(weight__gte=Decimal(str(weight)), region=r, recommanded=recommanded).order_by("price")[:1]
            if rs.exists():
                rates_ids.append(rs[0].id)

        return Rate.objects.filter(id__in=rates_ids).order_by(u'price')

    def __str__(self):
        return ("<Rate: max %.2fkg@%s, %.2f EUR>" % (self.weight, self.recommanded, self.price))
