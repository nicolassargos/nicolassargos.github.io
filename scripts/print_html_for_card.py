import os
import sys
import json

#F = Fungustober's notes

def generateHTML():
	output_html_file = "card.html"
	
	# Start creating the HTML file content
	html_content = '''<html>
<head>
	<title>Card</title>
	<meta property="og:title" content="Card" id="og-title">
	<meta property="og:type" content="website">
	<meta property="og:url" content="https://nicolassargos.github.io/card" id="og-url">
	<meta property="og:image" content="" id="og-image">
	<meta property="og:description" content="View custom Magic: The Gathering card" id="og-description">
	<meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:title" content="Card" id="twitter-title">
	<meta name="twitter:image" content="" id="twitter-image">
	<link rel="icon" type="image/x-icon" href="./img/favicon.png">
	<link rel="stylesheet" href="./resources/mana.css">
	<link rel="stylesheet" href="./resources/header.css">
	<link rel="stylesheet" href="./resources/card-text.css">
</head>
<script title="root">
	const rootPath = ".";
</script>
<style>
	@font-face {
		font-family: Beleren;
		src: url('./resources/beleren.ttf');
	}
	body {
		font-family: 'Helvetica', 'Arial', sans-serif;
		overscroll-behavior: none;
		margin: 0px;
		background-color: #f3f3f3;
	}
	a {
		text-decoration: none;
	}
	.banner-container {
		width: 100%;
		background-color: #bbbbbb;
		display: flex;
		justify-items: center;
		align-items: center;
	}
	.set-banner {
		font-family: Beleren;
		display: flex;
		gap: 30px;
		align-items: center;
		justify-items: center;
		font-size: 40px;
		color: #171717;
		margin: auto;
		padding-top: 10px;
		padding-bottom: 10px;
	}
	.set-banner img {
		width: 100px;
	}
	.image-grid {
		padding-top: 40px;
		width: 70%;
		max-width: 1000px;
		margin: auto;
		display: grid;
		grid-template-columns: minmax(200px, 2fr) minmax(200px, 2.5fr);
		gap: 30px;
		padding-bottom: 10px;
		justify-items: center;
	}
	.image-grid img {
		position: relative;
	}
	.card-image {
		float: left;
		width: 100%;
		max-width: 375px;
		height: auto;
		display: block;
	}
	.card-text {
		padding-top: 20px;
		padding-bottom: 20px;
		background: #fcfcfc;
		width: 100%;
		border: 1px solid #d5d9d9;
		border-top: 3px solid #171717;
		border-bottom: 3px solid #171717;
		border-radius: 6px;
		height: fit-content;
		min-height: 75%;
		margin-top: 3%;
		display: flex;
		flex-direction: column;
	}
	.designer-notes {
		padding-top: 10px;
		border-top: 1px solid #171717;
	}
	.card-text .printings {
		margin-top: auto;
		font-size: 12px;
		font-weight: bold;
		padding-bottom: 0px;
	}
	.printings {
		display: none;
	}
	.printings a {
		color: #1338be;
		text-decoration: none;
	}
	.printings a:hover {
		color: #0492c2;
	}
	.img-container {
		position: relative;
		align-self: center;
	}
	.img-container img {
		width: 100%;
		height: auto;
		border-radius: 3.733% / 2.677%;
	}
	.img-container .btn {
		background: url('./img/flip.png') no-repeat;
		background-size: contain;
		background-position: center;
		width: 15%;
		height: 11%;
		cursor: pointer;
		border: none;
		position: absolute;
		left: 50%;
		top: 48%;
		transform: translate(-50%, -50%);
		opacity: 0.5;
	}
	.img-container .btn:hover {
		background: url('./img/flip-hover.png') no-repeat;
		background-size: contain;
		background-position: center;
	}
	.img-container .h-img {
		transform: rotateY(0deg) rotate(90deg);
		width: 80%;
	}
	.img-container a {
		height: 100%;
		display: grid;
		justify-self: center;
		align-items: center;
		justify-items: center;
	}
	.img-container a > * {
		grid-row: 1;
		grid-column: 1;
	}
	.hidden {
		display: none;
	}
	/* Comments Section */
	.comments-container {
		width: 70%;
		max-width: 1000px;
		margin: 40px auto 60px auto;
		padding: 20px;
		background: #fcfcfc;
		border: 1px solid #d5d9d9;
		border-top: 3px solid #171717;
		border-radius: 6px;
	}
	.comments-header {
		font-family: Beleren;
		font-size: 24px;
		color: #171717;
		margin-bottom: 15px;
		padding-bottom: 10px;
		border-bottom: 2px solid #e0e0e0;
	}
	.comments-info {
		font-size: 13px;
		color: #666;
		margin-bottom: 20px;
		line-height: 1.6;
	}
</style>
<body>
	'''

	with open(os.path.join('scripts', 'snippets', 'header.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	html_content += '''

	<input type="text" id="display" class="hidden" value="cards-and-text"> <!-- here to make img-container-defs snippet work properly -->
	<div class="banner-container">
		<a class="set-banner" id="set-banner">
			<img class="set-logo" id="set-banner-logo">
			<div class="set-title" id="set-banner-title"></div>
		</a>
	</div>

	<div class="grid-container" id="grid">
	</div>

	<!-- Comments Section -->
	<div class="comments-container">
		<div class="comments-header">💬 Discussion</div>
		<div class="comments-info">
			Share your thoughts about this card! Comments are powered by GitHub and require a GitHub account to post.
		</div>
		<script src="https://utteranc.es/client.js"
			repo="nicolassargos/nicolassargos.github.io"
			issue-term="url"
			theme="github-light"
			crossorigin="anonymous"
			async>
		</script>
	</div>

	<script>
		let card_list_arrayified = [];
		let specialchars = "";

		document.addEventListener("DOMContentLoaded", async function () {
			'''

	with open(os.path.join('scripts', 'snippets', 'load-files.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet
	
	html_content += '''
			await fetch(rootPath + '/lists/all-sets.json')
					.then(response => response.json())
					.then(json => {
						set_list = json;
				}).catch(error => console.error('Error:', error));

			const params = new URLSearchParams(window.location.search);

			const set = params.get('set');
			const num = params.get('num');
			const name = params.get('name');

			for (const c of card_list_arrayified)
			{
				if (c.card_name == name && c.set == set && c.number == num)
				{
					card = c;
					break;
				}
			}

			var link = document.querySelector("link[rel~='icon']");
			link.href = rootPath + '/sets/' + set + '-files/icon.png';

			document.title = name;

			// Update Open Graph meta tags for social media previews
			const cardImageUrl = 'https://nicolassargos.github.io/sets/' + set + '-files/img/' + card.img_index + '.png';
			const pageUrl = window.location.href;
			const cardDescription = card.type + (card.mana_cost ? ' - ' + card.mana_cost : '');
			
			document.getElementById('og-title').setAttribute('content', name);
			document.getElementById('og-url').setAttribute('content', pageUrl);
			document.getElementById('og-image').setAttribute('content', cardImageUrl);
			document.getElementById('og-description').setAttribute('content', cardDescription);
			document.getElementById('twitter-title').setAttribute('content', name);
			document.getElementById('twitter-image').setAttribute('content', cardImageUrl);

			const banner = document.getElementById("set-banner");
			const banner_logo = document.getElementById("set-banner-logo");
			const banner_title = document.getElementById("set-banner-title");

			banner.href = rootPath + '/sets/' + set;
			banner_logo.src = rootPath + '/sets/' + set + '-files/icon.png';

			for (const set_stats of set_list.sets)
			{
				if (set_stats.set_code == set)
				{
					banner_title.innerHTML = set_stats.set_name;
					break;
				}
			}			

			document.getElementById("grid").appendChild(gridifyCard(card, false, card.rotated));

			other_printings = [];
			for (const c of card_list_arrayified)
			{
				if (c.rules_text == card.rules_text && c.card_name == card.card_name && c.type == card.type && !c.shape.includes("Token") && (c.set != card.set || c.number != card.number))
				{
					other_printings.push(c);
				}
			}

			if (other_printings.length > 0)
			{
				const printings = document.createElement("div");
				printings.className = "printings";
				printings.id = "other-printings";
				printings.innerText = "Other Printings: ";

				for (let i = 0; i < other_printings.length; i++)
				{
                    const printing = other_printings[i];
                    const setlink = document.createElement("a");
                    setlink.innerText = printing.set;

                    const url = new URL(rootPath + '/card', window.location.href.split('?')[0].split('/').slice(0, -1).join('/') + '/');
                    const params = {
                        set: printing.set,
                        num: printing.number,
                        name: printing.card_name
                    }
                    for (const key in params) {
                        url.searchParams.append(key, params[key]);
                    }
                    setlink.href = url.pathname + url.search;

                    printings.appendChild(setlink);
					if (i != other_printings.length - 1)
					{
						const dot = document.createElement("text");
						dot.innerText = " • ";
						printings.appendChild(dot);
					}
				}

				document.getElementById("card-text").appendChild(printings);
				document.getElementById("other-printings").style.display = "block";
			}
		});

		'''
	
	with open(os.path.join('scripts', 'snippets', 'tokenize-symbolize.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	html_content += '''

		function gridifyCard(card_stats, card_text = false, rotate_card = false, designer_notes = true) {
			card_stats = card;
			const card_name = card_stats.card_name;

		'''
	
	with open(os.path.join('scripts', 'snippets', 'img-container-defs.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	html_content += '''

		document.getElementById("search").addEventListener("keypress", function(event) {
			if (event.key === "Enter") {
				event.preventDefault();
				search();
			}
		});

		function search() {
			const url = new URL(rootPath + '/search', window.location.href.split('?')[0].split('/').slice(0, -1).join('/') + '/');
			url.searchParams.append('search', document.getElementById("search").value);
			window.location.href = url.pathname + url.search;
		}

		'''

	with open(os.path.join('scripts', 'snippets', 'random-card.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	html_content += '''
	</script>
</body>
</html>'''

	# Write the HTML content to the output HTML file
	with open(output_html_file, 'w', encoding='utf-8-sig') as file:
		file.write(html_content)

def generateIndividualCard(card):
	"""Generate individual HTML file for a specific card with proper meta tags"""
	set_code = card['set']
	card_num = card['number']
	card_name = card['card_name']
	
	# Create filename: card-SET-NUM.html
	filename = f"card-{set_code}-{card_num}.html"
	
	# Determine image URL
	if 'position' in card:
		img_suffix = f"{card['position']}"
	else:
		img_suffix = f"{card_num}_{card_name}"
	
	if card['shape'].lower().find('double') != -1:
		img_suffix += "_front"
	
	img_type = card.get('image_type', 'png')
	card_image_url = f"https://nicolassargos.github.io/sets/{set_code}-files/img/{img_suffix}.{img_type}"
	page_url = f"https://nicolassargos.github.io/{filename}"
	
	# Create description
	card_desc = card['type']
	if card.get('mana_cost'):
		card_desc += f" - {card['mana_cost']}"
	
	html_content = f'''<html>
<head>
	<title>{card_name}</title>
	<meta property="og:title" content="{card_name}">
	<meta property="og:type" content="website">
	<meta property="og:url" content="{page_url}">
	<meta property="og:image" content="{card_image_url}">
	<meta property="og:description" content="{card_desc}">
	<meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:title" content="{card_name}">
	<meta name="twitter:image" content="{card_image_url}">
	<link rel="icon" type="image/x-icon" href="./img/favicon.png">
	<link rel="stylesheet" href="./resources/mana.css">
	<link rel="stylesheet" href="./resources/header.css">
	<link rel="stylesheet" href="./resources/card-text.css">
</head>
<script title="root">
	const rootPath = ".";
</script>
<script>
	// Redirect to the query parameter version to maintain existing functionality
	window.location.href = `./card?set={set_code}&num={card_num}&name={card_name.replace("'", "\\'")}`;
</script>
<body>
	<p>Loading card: {card_name}...</p>
	<p>If you are not redirected, <a href="./card?set={set_code}&num={card_num}&name={card_name}">click here</a>.</p>
</body>
</html>'''
	
	with open(filename, 'w', encoding='utf-8-sig') as file:
		file.write(html_content)
