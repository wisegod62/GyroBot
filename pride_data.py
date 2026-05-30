# pride_data.py

GENDERS = {
    "agender": {
        "definition": "Refers to a person who does not identify with, relate to, or experience any internal gender identity.",
        "color": 0x7F8C8D,  # Gray
    },
    "bigender": {
        "definition": "Experiences two distinct gender identities, either simultaneously or varying over time.",
        "color": 0x9B59B6,  # Purple
    },
    "cisgender": {
        "definition": "A term used to describe a person whose gender identity aligns with the sex they were assigned at birth.",
        "color": 0x95A5A6,  # Light Slate Gray
    },
    "genderfluid": {
        "definition": "A gender identity or expression that shifts, changes, or flows over time.",
        "color": 0xFF69B4,  # Pink
    },
    "nonbinary": {
        "definition": "An umbrella term for gender identities that sit outside the strict male/female binary.",
        "color": 0xFFF000,  # Yellow
    },
    "transfem": {
        "definition": "Short for transfeminine. An umbrella term for transgender individuals who were assigned male at birth but identify more closely with femininity or womanhood.",
        "color": 0xFF8AD8,  # Soft Pastel Pink
    },
    "transgender": {
        "definition": "A person whose gender identity differs from the sex they were assigned at birth.",
        "color": 0x55CDFC,  # Trans Blue
    },
    "transmasc": {
        "definition": "Short for transmasculine. An umbrella term for transgender individuals who were assigned female at birth but identify more closely with masculinity or manhood.",
        "color": 0x60AFFF,  # Soft Pastel Blue
    },
    "genderqueer": {
        "definition": "Genderqueer is a gender identity used by people whose experience of gender falls outside traditional categories of exclusively male or female. Genderqueer people may identify with multiple genders, no gender, or a unique gender experience.",
        "color": 0x9C59D1,
    },
    
    "questioning": {
        "definition": "Questioning describes someone who is exploring or unsure of their gender identity. A questioning person may be learning more about their relationship with gender and may or may not eventually adopt a specific label.",
        "color": 0x808080,
    },
}

SEXUALITIES = {
    "androsexual": {
        "definition": "Attraction exclusively toward men, masculinity, or male anatomy, regardless of assigned sex.",
        "color": 0x2ECC71,  # Green
    },
    "asexual": {
        "definition": "A spectrum describing individuals who experience varying degrees of little to no sexual attraction.",
        "color": 0x000000,  # Black
    },
    "bisexual": {
        "definition": "An orientation describing attraction to two or more genders.",
        "color": 0x0038A8,  # Royal Blue
    },
    "gynesexual": {
        "definition": "Attraction exclusively toward women, femininity, or female anatomy, regardless of assigned sex.",
        "color": 0xE12984,  # Deep Pink
    },
    "heterosexual": {
        "definition": "An orientation describing romantic or sexual attraction to individuals of a different or opposing gender (often referred to as straight).",
        "color": 0x34495E,  # Dark Charcoal
    },
    "homosexual": {
        "definition": "An orientation describing romantic or sexual attraction to individuals of the same gender.",
        "color": 0xE67E22,  # Pride Orange
    },
    "lesbian": {
        "definition": "A woman or nonbinary person who is primarily attracted to women.",
        "color": 0xD62800,  # Orange-Red
    },
    "pansexual": {
        "definition": "An orientation describing attraction to people regardless of their gender identity.",
        "color": 0xFF007F,  # Hot Pink
    },
    "graysexual": {
        "definition": "Graysexual (or greysexual) is an identity on the asexual spectrum. Graysexual people experience sexual attraction rarely, weakly, infrequently, or only under specific circumstances.",
        "color": 0xA9A9A9,
    },
    
    "demisexual": {
        "definition": "Demisexual is an identity on the asexual spectrum. Demisexual people typically do not experience sexual attraction until they have formed a strong emotional bond with someone.",
        "color": 0x6E6E6E,
    },
    "queer": {
        "definition": "Queer is a broad and inclusive term used by some people whose sexual orientation, romantic orientation, gender identity, or overall experience falls outside traditional norms. Many people use queer as an umbrella term rather than a more specific label.",
        "color": 0xB57EDC,
    },
    
    "questioning": {
        "definition": "Questioning describes someone who is exploring or unsure of their sexual or romantic orientation. A questioning person may be learning more about themselves and may or may not eventually adopt a specific label.",
        "color": 0x808080,
    },
}

PRONOUNS = {
    "He/Him": {},
    "She/Her": {},
    "They/Them": {},
    "He/They": {},
    "She/They": {},
    "Any/All": {},
    "Ze/Zir/Zirs": {},
    "Xe/Xem/Xes": {},
}

QUEER_HISTORY = {
    "Alan Turing": {
        "definition": "Alan Turing was a genius whose WWII codebreaking saved millions of lives. He accidentally outed himself, and his security clearance was stripped. He was also forced to be subject to chemical castration. Because of this, he later commited suicide."
    },
    "Napoleon Bonaparte": {
        "definition": "There is no concrete evidence, but he was a very queer-friendly emperor and had a relationship with Tsar Alexander I that many percieve as homoerotic. He was married to women twice, so he may have been bisexual."
    },
    "James Buchanan": {
        "definition": "He was the only US President to remain a bachelor. His letters were burned by his family but some remain, with William Rufus King. Their correspondence mimicks that of romantic couples of the time."
    },
    "Alexander Von Humboldt": {
        "definition": "Von Humboldt's sexuality was very unclear, but he may have been gay."
    },
}

FLAGS = {

	"transgender": {
		"description": "A flag representing transgender people.",
		"creator": "Monica Helms",
		"year": 1999,
		"aliases": ["trans"],
		"type": "stripes",
		"colors": [
			"#5BCEFA",
			"#F5A9B8",
			"#FFFFFF",
			"#F5A9B8",
			"#5BCEFA"
		]
	},

	"nonbinary": {
		"description": "A flag representing nonbinary identities.",
		"creator": "Kye Rowan",
		"year": 2014,
		"aliases": ["nb"],
		"type": "stripes",
		"colors": [
			"#FFF430",
			"#FFFFFF",
			"#9C59D1",
			"#000000"
		]
	},

	"agender": {
		"description": "A flag representing agender people.",
		"creator": "Salem X",
		"year": 2014,
		"aliases": [],
		"type": "stripes",
		"colors": [
			"#000000",
			"#B9B9B9",
			"#FFFFFF",
			"#B8F483",
			"#FFFFFF",
			"#B9B9B9",
			"#000000"
		]
	},

	"bisexual": {
		"description": "A flag representing bisexual attraction.",
		"creator": "Michael Page",
		"year": 1998,
		"aliases": ["bi"],
		"type": "stripes",
		"colors": [
			"#D60270",
			"#9B4F96",
			"#0038A8"
		],
		"ratios": [2, 1, 2]
	},

	"pansexual": {
		"description": "A flag representing attraction regardless of gender.",
		"creator": "Unknown",
		"year": 2010,
		"aliases": ["pan"],
		"type": "stripes",
		"colors": [
			"#FF218C",
			"#FFD800",
			"#21B1FF"
		]
	},

	"asexual": {
		"description": "A flag representing asexuality.",
		"creator": "AVEN Community",
		"year": 2010,
		"aliases": ["ace"],
		"type": "stripes",
		"colors": [
			"#000000",
			"#A3A3A3",
			"#FFFFFF",
			"#800080"
		]
	},

	"aromantic": {
		"description": "A flag representing aromantic people.",
		"creator": "Cameron Whimsy",
		"year": 2014,
		"aliases": ["aro"],
		"type": "stripes",
		"colors": [
			"#3DA542",
			"#A7D379",
			"#FFFFFF",
			"#A9A9A9",
			"#000000"
		]
	},

	"aroace": {
		"description": "A flag representing people who are both aromantic and asexual.",
		"creator": "Sunset",
		"year": 2018,
		"aliases": ["aro-ace"],
		"type": "stripes",
		"colors": [
			"#E28C00",
			"#ECCB00",
			"#FFFFFF",
			"#62AEDC",
			"#203856"
		]
	},

	"lesbian": {
		"description": "The sunset lesbian flag.",
		"creator": "Emily Gwen",
		"year": 2018,
		"aliases": [],
		"type": "stripes",
		"colors": [
			"#D52D00",
			"#FF9A56",
			"#FFFFFF",
			"#D362A4",
			"#A30262"
		]
	},

	"genderqueer": {
		"description": "A flag representing genderqueer identities.",
		"creator": "Marilyn Roxie",
		"year": 2011,
		"aliases": ["gq"],
		"type": "stripes",
		"colors": [
			"#B57EDC",
			"#FFFFFF",
			"#4A8123"
		]
	},

	"intersex": {
		"description": "The intersex pride flag.",
		"creator": "Morgan Carpenter",
		"year": 2013,
		"aliases": [],
		"type": "svg",
		"elements": [
			{
				"type": "rect",
				"x": 0,
				"y": 0,
				"width": 900,
				"height": 600,
				"fill": "#FFD800"
			},
			{
				"type": "circle",
				"cx": 450,
				"cy": 300,
				"r": 120,
				"stroke": "#7902AA",
				"stroke_width": 20
			}
		]
	},

    "demisexual": {
        "description": "A flag representing demisexual people.",
        "creator": "AVEN Community",
        "year": 2010,
        "aliases": ["demi"],
        "type": "svg",
        "elements": [

            {
                "type": "rect",
                "x": 0,
                "y": 0,
                "width": 900,
                "height": 225,
                "fill": "#FFFFFF"
            },

            {
                "type": "rect",
                "x": 0,
                "y": 225,
                "width": 900,
                "height": 150,
                "fill": "#6E0170"
            },

            {
                "type": "rect",
                "x": 0,
                "y": 375,
                "width": 900,
                "height": 225,
                "fill": "#D2D2D2"
            },

            {
                "type": "polygon",
                "points": [
                    [0, 0],
                    [225, 300],
                    [0, 600]
                ],
                "fill": "#000000"
            }
        ]
    },

    "progress_pride": {
        "description": "The Progress Pride flag.",
        "creator": "Daniel Quasar",
        "year": 2018,
        "aliases": ["progress"],
        "type": "svg",
        "elements": [

            {
                "type": "rect",
                "x": 0,
                "y": 0,
                "width": 900,
                "height": 100,
                "fill": "#E40303"
            },
            {
                "type": "rect",
                "x": 0,
                "y": 100,
                "width": 900,
                "height": 100,
                "fill": "#FF8C00"
            },
            {
                "type": "rect",
                "x": 0,
                "y": 200,
                "width": 900,
                "height": 100,
                "fill": "#FFED00"
            },
            {
                "type": "rect",
                "x": 0,
                "y": 300,
                "width": 900,
                "height": 100,
                "fill": "#008026"
            },
            {
                "type": "rect",
                "x": 0,
                "y": 400,
                "width": 900,
                "height": 100,
                "fill": "#004DFF"
            },
            {
                "type": "rect",
                "x": 0,
                "y": 500,
                "width": 900,
                "height": 100,
                "fill": "#750787"
            },

            {
				"type": "polygon",
				"points": [
					[0, 0],
					[300, 300],
					[0, 600],
					[120, 600],
					[420, 300],
					[120, 0]
				],
				"fill": "#5BCEFA"
			},
			
			{
				"type": "polygon",
				"points": [
					[0, 60],
					[240, 300],
					[0, 540],
					[90, 540],
					[330, 300],
					[90, 60]
				],
				"fill": "#F5A9B8"
			},
			
			{
				"type": "polygon",
				"points": [
					[0, 120],
					[180, 300],
					[0, 480],
					[60, 480],
					[240, 300],
					[60, 120]
				],
				"fill": "#FFFFFF"
			},
			
			{
				"type": "polygon",
				"points": [
					[0, 0],
					[240, 300],
					[0, 600],
					[60, 600],
					[300, 300],
					[60, 0]
				],
				"fill": "#613915"
			},
			
			{
				"type": "polygon",
				"points": [
					[0, 0],
					[180, 300],
					[0, 600],
					[30, 600],
					[210, 300],
					[30, 0]
				],
				"fill": "#000000"
			}
        ]
    }
}
