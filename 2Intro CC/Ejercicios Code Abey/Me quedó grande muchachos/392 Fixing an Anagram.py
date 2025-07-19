def min_swaps_to_sort(s, target):
    """Calcula los intercambios mínimos necesarios para convertir la cadena s en target."""
    # Convertir cadenas en listas para trabajar con ellas
    s = list(s)
    target = list(target)
    
    swaps = []
    index_map = {char: [] for char in target}
    
    for idx, char in enumerate(target):
        index_map[char].append(idx)
    
    # Iterar sobre cada posición
    for i in range(len(s)):
        if s[i] == target[i]:
            continue
        
        # Buscar la posición de la letra correcta
        target_pos = index_map[target[i]].pop(0)
        
        # Realizar el intercambio
        if i != target_pos:
            s[i], s[target_pos] = s[target_pos], s[i]
            swaps.append(f"{i}:{target_pos}")
    
    return swaps

def format_swaps(swaps):
    """Formatea los intercambios como una cadena adecuada."""
    return ','.join(swaps)

def solve_anagram_problem(input_data):
    """Procesa los casos de prueba y devuelve los intercambios necesarios para cada uno."""
    lines = input_data.strip().split('\n')
    T = int(lines[0])
    results = []
    
    for i in range(1, T + 1):
        anagram, target = lines[i].split()
        swaps = min_swaps_to_sort(anagram, target)
        formatted_swaps = format_swaps(swaps)
        results.append(formatted_swaps)
    
    return ' '.join(results)

# Datos de entrada
input_data = """
31
RDEGLEED LEDGERED
CSSAWTHE SWATCHES
UMALSP AMPULS
BBOONN BONBON
UITTDEQ QUITTED
LSHSGHOPRUEA PLOUGHSHARES
RINEEHPASGOTNES PARTHENOGENESIS
GSSILIOANEMR REGIONALISMS
DARCTSIIINMN DISCRIMINANT
STNAEUEBMSSB SUBBASEMENTS
EO.UAATVNNENOINDVECDL EVADED.UNCONVENTIONAL
IGI.AESSDNNSSIUONWIC CAWING.INSIDIOUSNESS
OIS.OADCIFONTNNGNELCI OLDENING.CONFISCATION
TAHT.DSMEBDIIWTAGEEU WHETTED.DISAMBIGUATE
DISTOAFHZORADNME.IETIC FISHED.DEMOCRATIZATION
OCLZRAAPATEO.NLNYIITJ JALOPY.CENTRALIZATION
T.PYNOOSMICIANELLOXL PIXELS.MONOTONICALLY
RAMNMC.SOIRIBALEIYPINSOTTI INTERMISSION.COMPARABILITY
TRFOISREBISANGTS.ISENUSASRU AGRIBUSINESSES.FRUSTRATIONS
.DNGVTNSPEEHRIEIRNMRSUEEDA REPREHENDING.MISADVENTURES
STSTLNNAYUEGRTHA.BXIWMEAOE EXTRANEOUSLY.BANTAMWEIGHTS
UCAULIOGPCUMI.ENZIPLTRAAV POPULARIZING.ACCUMULATIVE
NT.MOTAIINSOENUHTNLNRRTSAUTBID TINTINNABULATIONS.THUNDERSTORM
ONC.TDRORDNNOGERETLFHSUHEEI UNDERCLOTHING.FORESHORTENED
APWLDAS..CLEELPYEHTATAN PENALTY.PLACATES.WHALED
RRPEESLGATD.EHRI.AEAEC ARCHER.PEERAGES.TAILED
TA.ERSNCYANOELMTIBIAV.O CITATION.OBSERVE.LAYMAN
ECEGPNTOOEKIAYR.DDWET.N KEYNOTED.COPIER.TWANGED
REUBF.TDJN.SXCEOOMEKUE SCOUT.FREEDMEN.JUKEBOX
DEGSVNBAREAID.EE.LAUMSLULT SALVAGED.TRIBUNES.MEDULLAE
.TLURSLULDENUTL.ECYIB CURLED.BUSTLE.NULLITY
"""

# Ejecución
print(solve_anagram_problem(input_data))