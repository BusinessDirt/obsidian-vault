import os
import re
import yaml

# Reference list of note names
note_names = [
    "Muskelaufbau", "Rechnerarchitektur", "Syntax und Semantik", "Logik und Diskrete Strukturen",
    "Algorithmen und Datenstrukturen", "Performance Enhancing Drugs", "Bananen-Protein-Muffins",
    "Quick Bolognese", "Pre-Workout Müsli", "Breakfast Joghurt", "Honig-Curry Hühnchen",
    "Bulking Protein Shake", "Schinkennudeln", "Protein Couscous", "ARP", "HTTP",
    "Lineare Gleichungssysteme", "Komplexe Zahlen", "Darwin-Term", "IP", "Enclomifen",
    "Endliche Automaten", "Allophon", "Magnetische Flussdichte", "Dirac-Gleichung",
    "Euklidischer Vektorraum", "Materiewelle", "Elektronensrahlröhre", "Syntax", "Anavar",
    "SMTP", "Semantik", "Muskelproteinsynthese", "POP3", "Aminosäuren", "TCP", "TLS",
    "Computerlinguistik", "Mechanotransduktion & Zellreparatur", "Chunking und Evaluation",
    "Dianabol", "Metformin HCl", "UDP", "Nebivolol", "Allele", "Kernfusion", "Logik",
    "Pragmatik", "Formale Sprachen", "Spin-Bahn-Kopplung", "DHCP",
    "Regeneration & Superkomposition", "Vektor", "FTP", "IMAP", "MAC", "Phonologie",
    "Dimension", "Knoten", "Morpheme", "Mengenlehre", "Variabilität", "Router", "ParseTree",
    "Rosuvastatin", "CYK-Algorithmus", "Bayes Theorem", "Elektrisches Feld",
    "ISO OSI-Schichtenmodell", "Haskell", "SSL", "Statistisches Parsing",
    "Von-Neumann-Architektur", "Trenbolon", "Impuls", "Morphologie",
    "Allgemeine Relativitätstheorie", "Phonem", "Tadalafil", "Parsing", "Astrophysik",
    "Vollständige Induktion", "Dopplereffekt", "Hamiltonoperator", "Russellsche Antinomie",
    "Ezetimibe", "Merkmalsstrukturen", "Unifikationsgrammatik", "Telmisartan", "Losartan",
    "Feinstruktur", "AdBlue", "Kepler", "Hardy-Weinberg-Gleichgewicht", "DNS",
    "Selektive katalytische Reduktion", "Ammoniak", "Matrix", "Laktatazidose",
    "Komplexe Sätze", "Rhabdomyolyse", "Myhill-Nerode-Theorem", "Lineare Abbildungen",
    "Konstituentenanalyse", "Dependenzgrammatik", "Binärbaum", "Reguläre Ausdrücke",
    "Zufallsvariablen", "Lorentzkraft", "Relationen", "Stochastische Unabhängigkeit",
    "Cyclic Redundancy Check", "Kontextfreie Grammatik", "NAT", "SLAAC", "Allomorph",
    "Magnetisches Feld", "Spezielle Relativitätstheorie", "X-Bar-Theorie", "Isocyansäure",
    "Liste", "Harnstoff", "IPsec", "Wort", "Natürliche Sprache", "Elektromagnetische Strahlung",
    "Phonetik", "Wortstruktur", "Ambiguität", "Heap Sort", "NDP", "Hormonelle Steuerung",
    "NLTK", "Baum", "Clomifen", "Abbildungen", "Graph", "Künstliche Intelligenz",
    "Pumping-Lemma", "Induktion", "Gruppen", "Ringe", "Körper", "Kleene-Stern"
]

# Tag mapping based on keywords
tag_keywords = {
    "Mathe": ["Mathe", "Mathematik", "Gleichung", "Menge", "Vektor", "Matrix", "Zahl", "Theorem", "Beweis", "Induktion", "Abbildung"],
    "Informatik": ["Informatik", "Rechner", "Netzwerk", "Protokoll", "Algorithmus", "Programmierung", "Computer", "Parsing", "Automaten"],
    "Linguistik": ["Linguistik", "Sprache", "Wort", "Phon", "Syntax", "Semantik", "Morphologie", "Grammatik", "Pragmatik"],
    "Physik": ["Physik", "Energie", "Kraft", "Quanten", "Feld", "Relativität", "Teilchen", "Welle", "Strahlung"],
    "Biologie": ["Biologie", "Zelle", "Protein", "Muskel", "DNS", "Allele", "Hormon", "Genetik"],
    "Pharmakologie": ["Pharmakologie", "Medikament", "Wirkstoff", "Hormon", "Steroid", "PED", "SARM", "Blocker"],
    "Training": ["Training", "Muskel", "Hypertrophie", "Krafttraining"],
    "Rezepte": ["Rezept", "Kochen", "Zutaten", "Zubereitung"]
}

def process_file(filepath, filename_no_ext):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter and body
    frontmatter_content = ""
    body = content
    fm_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if fm_match:
        frontmatter_content = fm_match.group(1)
        body = content[fm_match.end():]

    # 1. Update Tags
    existing_tags = []
    data = {}
    if frontmatter_content:
        # Pre-process frontmatter to handle unquoted #tags which YAML treats as comments
        processed_fm = re.sub(r'(\s*-\s*)#(\w+)', r'\1\2', frontmatter_content)
        try:
            data = yaml.safe_load(processed_fm)
            if data and 'tags' in data:
                raw_tags = data['tags']
                if isinstance(raw_tags, list):
                    existing_tags = [str(t).lstrip('#') for t in raw_tags if t is not None]
                elif isinstance(raw_tags, str):
                    existing_tags = [raw_tags.lstrip('#')]
        except Exception as e:
            print(f"Error parsing frontmatter in {filename_no_ext}: {e}")

    new_tags = set(existing_tags)
    for tag, keywords in tag_keywords.items():
        for kw in keywords:
            # Use word boundaries for keywords to avoid false positives (e.g., Rezeptor -> Rezept)
            pattern = re.compile(r'\b' + re.escape(kw) + r'\b', re.IGNORECASE)
            if pattern.search(body):
                new_tags.add(tag)
                break
    
    # Update frontmatter if tags changed or to clean up #
    if set(existing_tags) != new_tags or '#' in frontmatter_content:
        if data is None: data = {}
        data['tags'] = sorted(list(new_tags))
        # Ensure other fields are preserved
        frontmatter_content = yaml.dump(data, allow_unicode=True, default_flow_style=False).strip()

    # 2. Linking
    # Identify blocks to exclude
    placeholders = []
    
    def replace_block(match):
        placeholder = f"__BLOCK_{len(placeholders)}__"
        placeholders.append(match.group(0))
        return placeholder

    # Exclude code blocks, inline code, latex, existing links
    # Order matters: larger blocks first
    body_placeholder = body
    # Code blocks
    body_placeholder = re.sub(r'```[\s\S]*?```', replace_block, body_placeholder)
    # Inline code
    body_placeholder = re.sub(r'`.*?`', replace_block, body_placeholder)
    # LaTeX blocks
    body_placeholder = re.sub(r'\$\$[\s\S]*?\$\$', replace_block, body_placeholder)
    body_placeholder = re.sub(r'\$[^$]*?\$', replace_block, body_placeholder)
    # Existing links
    body_placeholder = re.sub(r'\[\[.*?\]\]', replace_block, body_placeholder)
    body_placeholder = re.sub(r'\[.*?\]\(.*?\)', replace_block, body_placeholder)

    # Now link terms
    changed = False
    for note in note_names:
        if note == filename_no_ext:
            continue
        
        # Regex for the note name as a whole word
        # We use a lambda to only replace the first occurrence
        def link_replacer(match, note_name=note):
            nonlocal changed
            changed = True
            return f"[[{note_name}]]"

        # Search for note name as whole word, case sensitive or at start of sentence
        pattern = re.compile(r'\b' + re.escape(note) + r'\b')
        
        # We only want to replace the first occurrence in the placeholder body
        if pattern.search(body_placeholder):
            body_placeholder = pattern.sub(link_replacer, body_placeholder, count=1)

    # Put blocks back
    for i, original in enumerate(placeholders):
        body_placeholder = body_placeholder.replace(f"__BLOCK_{i}__", original)

    new_content = f"---\n{frontmatter_content}\n---\n{body_placeholder}"
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

directory = "/Users/dp1key/Documents/Obsidian/obsidian-vault/02 - Areas/"
files = [f for f in os.listdir(directory) if f.endswith(".md")]

for f in files:
    filename_no_ext = os.path.splitext(f)[0]
    filepath = os.path.join(directory, f)
    try:
        updated = process_file(filepath, filename_no_ext)
        if updated:
            print(f"Updated: {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
