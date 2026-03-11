import os
import sys
import json

#F = Fungustober's notes

def generateHTML(codes):
	output_html_file = "search.html"

	# Start creating the HTML file content
	html_content = '''<html>
<head>
	<title>Search</title>
	<link rel="icon" type="image/x-icon" href="./img/search.png">
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
	.button-grid {
		width: 70%;
		max-width: 1200px;
		height: 40px;
		margin: auto;
		display: grid;
		grid-template-columns: 4fr 1fr;
		gap: 10px;
		padding-top: 20px;
		padding-bottom: 20px;
		justify-items: center;
	}
	.prev-next-btns {
		width: 100%;
		height: 40px;
		margin: auto;
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 5px;
		align-items: center;
	}
	button {
		background-color: #fafafa;
		border: 1px solid #d5d9d9;
		border-radius: 8px;
		box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;
		color: #171717;
		cursor: pointer;
		font-size: 13px;
		width: 100%;
		height: 35px;
		min-width: 85px;
	}
	button:hover {
		background-color: #ffffff;
	}
	button:focus {
		border-color: #171717;
		box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;
		outline: 0;
	}
	button:disabled, select:disabled {
		cursor: auto;
		background-color: #f7fafa;
		font-style: italic;
		box-shadow: none;
		color: #cccccc;
	}
	.button-grid .results-text {
		margin-right: -3px;
	}
	.button-grid .select-text {
		width: 100%;
		display: flex;
		align-items: center;
		justify-content: left;
		gap: 8px;
		font-size: 14.5px;
		text-align: center;
	}
	select {
		background-color: #fafafa;
		border: 1px solid #d5d9d9;
		border-radius: 8px;
		box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;
		text-align: center;
		color: #171717;
		font-size: 13px;
		height: 30px;
	}
	.grid-container {
		display: grid;
		grid-template-columns: auto;
		max-width: 1200px;
		margin: auto;
	}
	.image-grid-container {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr 1fr;
		width: 70%;
		max-width: 1200px;
		margin: auto;
		gap: 5px;
		justify-items: center;
	}
	@media ( max-width: 750px ) {
		.image-grid-container {
			grid-template-columns: 1fr 1fr;	
		}
	}
	.image-grid {
		width: 70%;
		margin: auto;
		display: grid;
		grid-template-columns: minmax(150px, 1fr) minmax(300px, 2fr);
		gap: 50px;
		padding-bottom: 10px;
		justify-items: left;
	}
	.image-grid img {
		position: relative;
	}
	.card-image {
		float: left;
		width: 100%;
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
	}
	.img-container {
		position: relative;
		width: 100%;
		align-self: center;
	}
	.img-container img {
		width: 100%;
		height: auto;
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
		border-radius: 0px;
		box-shadow: none;
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
	.img-container .hidden-text {
		position: absolute;
		font-family: Beleren;
		top: 5%;
		left: 9%;
		font-size: .97vw;
		color: rgba(0, 0, 0, 0);
	}
	.no-results {
		display: none;
		text-align: center;
		padding-top: 100px;
		padding-bottom: 100px;
		width: 100%;
	}
	.no-results img {
		width: 150px;
		margin-bottom: 20px;
		opacity: 0.3;
		filter: drop-shadow(0 0 4px #000);
	}
	.no-results h1 {
		font-family: Beleren;
		color: #494949;
		margin: 0;
		font-size: 40px;
	}
	.no-results p {
		color: #797979;
		font-size: 18px;
		margin-top: 10px;
	}
	/* Quick Filters Panel */
	.quick-filters {
		width: 70%;
		max-width: 1200px;
		margin: 20px auto 10px auto;
		padding: 15px;
		background: white;
		border: 1px solid #d5d9d9;
		border-radius: 8px;
		box-shadow: rgba(213, 217, 217, .3) 0 2px 5px 0;
	}
	.filter-section {
		margin-bottom: 12px;
	}
	.filter-section:last-child {
		margin-bottom: 0;
	}
	.filter-label {
		font-size: 12px;
		font-weight: 600;
		color: #666;
		margin-bottom: 6px;
		text-transform: uppercase;
		letter-spacing: 0.5px;
	}
	.filter-buttons {
		display: flex;
		gap: 6px;
		flex-wrap: wrap;
	}
	.filter-btn {
		padding: 6px 12px;
		font-size: 13px;
		min-width: auto;
		height: auto;
		border-radius: 16px;
		background-color: #fafafa;
		border: 1px solid #d5d9d9;
		cursor: pointer;
		transition: all 0.2s;
	}
	.filter-btn:hover {
		background-color: #f0f0f0;
		border-color: #999;
	}
	.filter-btn.active {
		background-color: #4a90e2;
		color: white;
		border-color: #4a90e2;
	}
	.filter-btn.color-w { border-left: 3px solid #f0f0c8; }
	.filter-btn.color-u { border-left: 3px solid #0e68ab; }
	.filter-btn.color-b { border-left: 3px solid #150b00; }
	.filter-btn.color-r { border-left: 3px solid #d3202a; }
	.filter-btn.color-g { border-left: 3px solid #00733e; }
	.filter-btn.color-c { border-left: 3px solid #ccc; }
	.filter-btn.color-m { border-left: 3px solid linear-gradient(90deg, #f0f0c8, #0e68ab, #150b00); }
	/* Filter Chips */
	.filter-chips {
		width: 70%;
		max-width: 1200px;
		margin: 0 auto 10px auto;
		display: flex;
		gap: 6px;
		flex-wrap: wrap;
		min-height: 24px;
	}
	.filter-chip {
		display: inline-flex;
		align-items: center;
		gap: 6px;
		padding: 4px 10px;
		background-color: #e3f2fd;
		border: 1px solid #90caf9;
		border-radius: 16px;
		font-size: 12px;
		color: #1565c0;
		font-weight: 500;
	}
	.filter-chip .remove {
		cursor: pointer;
		font-weight: bold;
		opacity: 0.7;
		padding: 0 3px;
	}
	.filter-chip .remove:hover {
		opacity: 1;
	}
</style>
<body>
	'''

	with open(os.path.join('scripts', 'snippets', 'header.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	html_content += '''
	
	<!-- Quick Filters Panel -->
	<div class="quick-filters">
		<div class="filter-section">
			<div class="filter-label">Colors</div>
			<div class="filter-buttons">
				<button class="filter-btn color-w" data-filter="c:w" title="White">W</button>
				<button class="filter-btn color-u" data-filter="c:u" title="Blue">U</button>
				<button class="filter-btn color-b" data-filter="c:b" title="Black">B</button>
				<button class="filter-btn color-r" data-filter="c:r" title="Red">R</button>
				<button class="filter-btn color-g" data-filter="c:g" title="Green">G</button>
				<button class="filter-btn color-c" data-filter="c:c" title="Colorless">C</button>
				<button class="filter-btn color-m" data-filter="c:m" title="Multicolor">M</button>
			</div>
		</div>
		<div class="filter-section">
			<div class="filter-label">Card Types</div>
			<div class="filter-buttons">
				<button class="filter-btn" data-filter="t:creature">Creature</button>
				<button class="filter-btn" data-filter="t:instant">Instant</button>
				<button class="filter-btn" data-filter="t:sorcery">Sorcery</button>
				<button class="filter-btn" data-filter="t:enchantment">Enchantment</button>
				<button class="filter-btn" data-filter="t:artifact">Artifact</button>
				<button class="filter-btn" data-filter="t:planeswalker">Planeswalker</button>
				<button class="filter-btn" data-filter="t:land">Land</button>
			</div>
		</div>
		<div class="filter-section">
			<div class="filter-label">Rarity</div>
			<div class="filter-buttons">
				<button class="filter-btn" data-filter="r:common">Common</button>
				<button class="filter-btn" data-filter="r:uncommon">Uncommon</button>
				<button class="filter-btn" data-filter="r:rare">Rare</button>
				<button class="filter-btn" data-filter="r:mythic">Mythic</button>
			</div>
		</div>
	</div>

	<!-- Filter Chips Display -->
	<div class="filter-chips" id="filter-chips">
	</div>

	<div class="button-grid">
		<div class="select-text"><div class="results-text" id="results-text">Loading ...</div>Cards displayed as<select name="display" id="display"><option value="cards-only">Cards Only</option><option value="cards-text">Cards + Text</option></select>sorted by<select name="sort-by" id="sort-by"><option value="name">Name</option><option value="set-code">Set / Number</option><option value="mv">Mana Value</option><option value="color">Color</option><option value="rarity">Rarity</option><option value="cube">Cube</option></select> : <select name="sort-order" id="sort-order"><option value="ascending">Asc</option><option value="descending">Desc</option></select></div>		
		<div class="prev-next-btns">
			<button type="submit" onclick="previousPage()" id="prevBtn" disabled>< Previous</button>
			<button type="submit" onclick="nextPage()" id="nextBtn">Next 30 ></button>
		</div>
	</div>

	<div class="grid-container" id="grid">
	</div>

	<div class="image-grid-container" id="imagesOnlyGrid">
	</div>

	<div id="no-results" class="no-results">
		<img src="./img/deck.png">
		<h1>No cards found</h1>
		<p>Your search didn't match any cards. Try adjusting your search terms.</p>
	</div>

	<div class="button-grid" id="footer">
		<div></div>
		<div class="prev-next-btns">
			<button type="submit" onclick="previousPage()" id="prevBtn-footer" disabled>< Previous</button>
			<button type="submit" onclick="nextPage()" id="nextBtn-footer">Next 30 ></button>
		</div>
	</div>

	<script>
		let page = 0;
		let pageCount = 30;
		let search_results = [];
		let card_list_arrayified = [];
		let specialchars = "";
		let sets_json = {};

		document.addEventListener("DOMContentLoaded", async function () {
			'''

	with open(os.path.join('scripts', 'snippets', 'load-files.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	html_content += '''

			await fetch(rootPath + '/lists/all-sets.json')
					.then(response => response.json())
					.then(data => {
						sets_json = data; 
				}).catch(error => console.error('Error:', error));

			card_list_arrayified = card_list.cards;

			if (sessionStorage.getItem("display") != "cards-only")
			{
				cardGrid = document.getElementById("grid");
			}
			else
			{
				cardGrid = document.getElementById("imagesOnlyGrid");
			}

			card_list_arrayified.sort(compareFunction);

			// refresh page values
			const params = new URLSearchParams(window.location.search);
			page = params.get("page") ? params.get("page") : 0;
			document.getElementById("search").value = params.get("search") ? decodeURIComponent(params.get("search")) : "";

			if (sessionStorage.getItem("sortMethod"))
			{
				document.getElementById("sort-by").value = sessionStorage.getItem("sortMethod");				
			}
			if (sessionStorage.getItem("display"))
			{
				document.getElementById("display").value = sessionStorage.getItem("display");				
			}

			displayStyle = document.getElementById("display").value;
			setCardView();

			// initial search on load
			preSearch(false);
		});

		function displayChangeListener() {
			displayStyle = document.getElementById("display").value;
			sessionStorage.setItem("display", displayStyle);
			sessionStorage.setItem("sortMethod", document.getElementById("sort-by").value);

			setCardView();

			preSearch(false);
		}

		document.getElementById("sort-by").onchange = displayChangeListener;
		document.getElementById("display").onchange = displayChangeListener;
		document.getElementById("sort-order").onchange = displayChangeListener;

		// Quick Filter Buttons Handler
		document.querySelectorAll('.filter-btn').forEach(btn => {
			btn.addEventListener('click', function(e) {
				e.preventDefault();
				const filter = this.getAttribute('data-filter');
				const searchBox = document.getElementById('search');
				let currentSearch = searchBox.value.trim();
				
				// Toggle active state
				if (this.classList.contains('active')) {
					// Remove filter
					this.classList.remove('active');
					currentSearch = currentSearch.split(' ').filter(term => term !== filter).join(' ');
				} else {
					// Add filter
					this.classList.add('active');
					currentSearch = currentSearch ? currentSearch + ' ' + filter : filter;
				}
				
				searchBox.value = currentSearch.trim();
				updateFilterChips();
				preSearch(true);
			});
		});

		// Update Filter Chips based on search query
		function updateFilterChips() {
			const searchBox = document.getElementById('search');
			const searchTerms = searchBox.value.trim().split(/\s+/);
			const chipsContainer = document.getElementById('filter-chips');
			chipsContainer.innerHTML = '';
			
			// Update button states and create chips
			document.querySelectorAll('.filter-btn').forEach(btn => {
				const filter = btn.getAttribute('data-filter');
				if (searchTerms.includes(filter)) {
					btn.classList.add('active');
					
					// Create chip
					const chip = document.createElement('div');
					chip.className = 'filter-chip';
					chip.innerHTML = `<span>${filter}</span><span class="remove" title="Remove filter">×</span>`;
					chip.querySelector('.remove').addEventListener('click', () => removeFilter(filter));
					chipsContainer.appendChild(chip);
				} else {
					btn.classList.remove('active');
				}
			});
		}

		// Remove a filter
		function removeFilter(filter) {
			const searchBox = document.getElementById('search');
			let currentSearch = searchBox.value.trim();
			currentSearch = currentSearch.split(' ').filter(term => term !== filter).join(' ');
			searchBox.value = currentSearch.trim();
			updateFilterChips();
			preSearch(true);
		}

		// Update chips on search input
		document.getElementById('search').addEventListener('input', updateFilterChips);
		
		// Initial chip update
		updateFilterChips();

		window.addEventListener('popstate', function(event) {
			let params = decodeURIComponent(window.location.href.indexOf("?search") == -1 ? "" : window.location.href.substring(window.location.href.indexOf("?search") + 8), (window.location.href.indexOf("page=") == -1 ? window.location.href.length : window.location.href.indexOf("page=")));
			document.getElementById("search").value = (params.indexOf("&page=") == -1 ? params.replaceAll("+", " ") : params.substring(0, params.indexOf("&page=")).replaceAll("+", " "));
			page = window.location.href.indexOf("page=") == -1 ? 0 : parseInt(window.location.href.substring(window.location.href.indexOf("page=") + 5)) - 1;

			preSearch(false);
		});

		function setCardView() {
			imagesOnlyGrid.style.display = displayStyle == "cards-only" ? '' : 'none';
			grid.style.display = displayStyle == "cards-only" ? 'none' : '';
		}

		'''

	with open(os.path.join('scripts', 'snippets', 'compare-function.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	#F: I've added in a bunch of additional variables to allow people to search DFCs by info on their back faces
	#F: For example, let's say I want to find Delver of Secrets by searching for a 3/2 (which is the p/t of Insectile Aberration)
	#F: Alas, I don't know how to incorporate this into the search, so I will leave that up to other people.
	html_content += '''

		function preSearch(setNewState) {
			const searchTerms = document.getElementById("search").value.toLowerCase();
			const tokens = tokenizeTerms(searchTerms) || [];
			const sortBySelect = document.getElementById("sort-by");
			const sortOrderSelect = document.getElementById("sort-order");

			sortBySelect.disabled = false;
			sortOrderSelect.disabled = false;

			tokens.forEach(token => {
				if (token.startsWith("sort:")) {
					const val = token.substring(5);
					const map = {
						"name": "name",
						"set": "set-code",
						"mv": "mv",
						"color": "color",
						"rarity": "rarity",
						"cube": "cube"
					};
					if (map[val]) {
						const option = Array.from(sortBySelect.options).find(opt => opt.value === map[val]);
						if (option) {
							sortBySelect.value = map[val];
							sortBySelect.disabled = true;
						}
					}
				}
				if (token.startsWith("direction:")) {
					const val = token.substring(10);
					const map = {
						"asc": "ascending",
						"desc": "descending"
					};
					if (map[val]) {
						const option = Array.from(sortOrderSelect.options).find(opt => opt.value === map[val]);
						if (option) {
							sortOrderSelect.value = map[val];
							sortOrderSelect.disabled = true;
						}
					}
				}
			});

			card_list_arrayified.sort(compareFunction);
			if (document.getElementById("sort-order").value == "descending")
			{
				card_list_arrayified.reverse();
			}
			search_results = [];
			page = setNewState ? 0 : page;

			search(setNewState);
		}

		function search(setNewState) {
			searchTerms = document.getElementById("search").value.toLowerCase();

			if (searchTerms != "")
			{
				if (setNewState)
				{
					let url = (window.location.href.indexOf("?") == -1 ? new URL(window.location.href) : new URL(window.location.href.substring(0, window.location.href.indexOf("?"))));
					let params = new URLSearchParams(url.search);
					params.append("search", searchTerms);
					history.pushState({}, '', url.pathname + '?' + params.toString());
				}
			}
			else
			{
				if (setNewState)
				{
					let url = (window.location.href.indexOf("?") == -1 ? new URL(window.location.href) : new URL(window.location.href.substring(0, window.location.href.indexOf("?"))));
					let params = new URLSearchParams(url.search);
					params.delete("search");
					history.pushState({}, '', url.pathname + '' + params.toString());
				}
			}

			if (displayStyle == "cards-only")
			{
				cardGrid = document.getElementById("imagesOnlyGrid");
			}
			else
			{
				cardGrid = document.getElementById("grid");
			}
			cardGrid.innerHTML = "";

			for (const card of card_list_arrayified) {
				if (card.shape.includes("token") && !searchTerms.includes("+t:token") && !searchTerms.includes("t:token"))
				{
					continue;
				}

				if (card.type.includes("Basic") && !searchTerms.includes("+t:basic") && !searchTerms.includes("t:basic"))
				{
					continue;
				}

				if (card.rarity.includes("masterpiece") && !searchTerms.includes("+r:masterpiece") && !searchTerms.includes("+r:mp") && !searchTerms.includes("t:basic"))
				{
					continue;
				}

				searched = searchAllTokens(card, tokenizeTerms(searchTerms));

				if (searched && !containsCard(search_results, card))
				{
					search_results.push(card);
				}
			}

			if (searchTerms != "")
			{
				document.getElementById("results-text").innerText = search_results.length + (search_results.length == 1 ? " result found." : " results found.");
			}
			else
			{
				document.getElementById("results-text").innerText = "";
			}

			if (search_results.length == 0) {
				document.getElementById("no-results").style.display = "block";
				document.getElementById("footer").style.display = "none";
			} else {
				document.getElementById("no-results").style.display = "none";
				document.getElementById("footer").style.display = "grid";
			}

			if (page != 0)
			{
				document.getElementById("prevBtn").disabled = false;
				document.getElementById("prevBtn-footer").disabled = false;
			}
			else
			{
				document.getElementById("prevBtn").disabled = true;
				document.getElementById("prevBtn-footer").disabled = true;
			}

			// set text of Next to match number of displayed images
			displayStyle = document.getElementById("display").value;
				pageCount = displayStyle == "cards-only" ? 60 : 30;
				document.getElementById("nextBtn").innerText = "Next " + pageCount + " >";
				document.getElementById("nextBtn-footer").innerText = "Next " + pageCount + " >";

				// really awesome code block to fix the URL when switching from Cards + Text view to Cards Only view
				while ((pageCount * page) > search_results.length)
				{
					page = page - 1;

					let url = (window.location.href.indexOf("page=") == -1 ? new URL(window.location.href) : new URL(window.location.href.substring(0, window.location.href.indexOf("page="))));
				let params = new URLSearchParams(url.search);
				params.append("page", page + 1);
				history.replaceState({}, '', url.pathname + '?' + params.toString());
				}

			for (let i = (pageCount * page); i < Math.min((pageCount * (page + 1)), search_results.length); i++)
			{
				cardGrid.appendChild(gridifyCard(search_results[i]));
			}

			if (search_results.length <= (pageCount * (page + 1)))
			{
				document.getElementById("nextBtn").disabled = true;
				document.getElementById("nextBtn-footer").disabled = true;
			}
			else
			{
				document.getElementById("nextBtn").disabled = false;
				document.getElementById("nextBtn-footer").disabled = false;
			}
		}

		function containsCard(list, card)
		{
			for (const li of list)
			{
				if (li.card_name == card.card_name && li.type == card.type && li.rules_text == card.rules_text)
				{
					return true;
				}
			}

			return false;
		}

		'''

	with open(os.path.join('scripts', 'snippets', 'search-defs.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	with open(os.path.join('scripts', 'snippets', 'tokenize-symbolize.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	html_content += '''

		function gridifyCard(card_stats, card_text = false, rotate_card = false, designer_notes = false) {
			const card_name = card_stats.card_name;

			if (displayStyle == "cards-only")
			{
				return buildImgContainer(card_stats, true, rotate_card);
			}

		'''

	with open(os.path.join('scripts', 'snippets', 'img-container-defs.txt'), encoding='utf-8-sig') as f:
		snippet = f.read()
		html_content += snippet

	html_content += '''

		function hasAllChars(strOut, strIn) {
			let retVal = true;

			for (let i = 0; i < strIn.length; i++)
			{
				if (!strOut.includes(strIn.charAt(i)))
				{
					retVal = false;
				}
			}

			return retVal;
		}

		function hasNoChars(strOut, strIn) {
			let retVal = true;

			for (let i = 0; i < strIn.length; i++)
			{
				if (strOut.includes(strIn.charAt(i)))
				{
					retVal = false;
				}
			}

			return retVal;
		}

		function hasAllAndMoreChars(strOut, strIn) {
			let retVal = true;

			for (let i = 0; i < strIn.length; i++)
			{
				if (!strOut.includes(strIn.charAt(i)))
				{
					retVal = false;
				}
			}

			return retVal && (strOut.length > strIn.length);
		}

		document.getElementById("search").addEventListener("keypress", function(event) {
			if (event.key === "Enter") {
			event.preventDefault();
			preSearch(true);
			}
		});

		function previousPage() {
			page = page - 1;
			cardGrid.innerHTML = "";

			let url = (window.location.href.indexOf("page=") == -1 ? new URL(window.location.href) : new URL(window.location.href.substring(0, window.location.href.indexOf("page="))));
			let params = new URLSearchParams(url.search);
			if (page != 0)
			{
				params.append("page", page + 1);
			}
			history.pushState({}, '', url.pathname + '?' + params.toString());

			for (let i = (pageCount * page); i < Math.min((pageCount * (page + 1)), search_results.length); i++)
			{
				cardGrid.appendChild(gridifyCard(search_results[i]));
			}

			document.getElementById("nextBtn").disabled = false;
			document.getElementById("nextBtn-footer").disabled = false;
			if (page == 0)
			{
				document.getElementById("prevBtn").disabled = true;
				document.getElementById("prevBtn-footer").disabled = true;
			}

			document.body.scrollTop = 0; // For Safari
				document.documentElement.scrollTop = 0; // For real browsers
		}

		function nextPage() {
			page = page + 1;
			
			let url = (window.location.href.indexOf("page=") == -1 ? new URL(window.location.href) : new URL(window.location.href.substring(0, window.location.href.indexOf("page="))));
			let params = new URLSearchParams(url.search);
			params.append("page", page + 1);
			history.pushState({}, '', url.pathname + '?' + params.toString());

			cardGrid.innerHTML = "";

			for (let i = (pageCount * page); i < Math.min((pageCount * (page + 1)), search_results.length); i++)
			{
				cardGrid.appendChild(gridifyCard(search_results[i]));
			}

			document.getElementById("prevBtn").disabled = false;
			document.getElementById("prevBtn-footer").disabled = false;
			if (search_results.length <= (pageCount * (page + 1)))
			{
				document.getElementById("nextBtn").disabled = true;
				document.getElementById("nextBtn-footer").disabled = true;
			}

			document.body.scrollTop = 0; // For Safari
				document.documentElement.scrollTop = 0; // For real browsers
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

	print(f"HTML file saved as {output_html_file}")