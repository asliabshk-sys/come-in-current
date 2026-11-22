"""Space prose in this iteration's new reports;preserve code and link targets."""
from pathlib import Path
import re

here=Path(__file__).resolve().parent
replacements={
 'Task1audit':'Task 1 audit','Task1':'Task 1','Task2is':'Task 2 is','Task2':'Task 2',
 'Expectedwork/HEAD':'Expected work / HEAD','113bounded':'113 bounded',
 'separateUNVERIFIEDclaim':'separate UNVERIFIED claim','dynamicnext':'dynamic next',
 '179registrations':'179 registrations','387parameters':'387 parameters','216defaults':'216 defaults',
 '27Queryparameters':'27 Query parameters','60models':'60 models',
 'staysOPEN/VALIDATIONBLOCKED':'stays OPEN / VALIDATION BLOCKED',
 'remainsOPEN/VALIDATIONBLOCKED':'remains OPEN / VALIDATION BLOCKED',
 '39historicalXMLs':'39 historical XMLs','39historical':'39 historical',
 'recordedhash':'recorded hash','Saved67declarations':'Saved 67 declarations',
 'savedmetadata':'saved metadata','DBcapture':'DB capture','rawvalidatoroptions':'raw validator options',
 'Historicalbundle':'Historical bundle','successfulcompiled':'successfully compiled',
 'providerTEST':'provider TEST','externaldelivery':'external delivery',
 'GenuineauthorizedTESTdelivery':'Genuine authorized TEST delivery',
 'currentcredentials/providercalls':'current credentials / provider calls',
 'Localguards/syntheticTLS':'Local guards / synthetic TLS',
 'ActualauthorizedTLS':'Actual authorized TLS','DBroles/secretcustody':'DB roles / secret custody',
 'The11proposed':'The 11 proposed','fiveMarkdown':'five Markdown','DBoperations':'DB operations',
 'the5finalreports':'the 5 final reports','newmanifest':'new manifest',
 'original3contradicted':'original 3 contradicted',
 'unresolvedHIGHSEC-01and':'unresolved HIGH SEC-01 and',
 'remainsREVIEWPENDINGand':'remains REVIEW PENDING and','authorizeTask 2':'authorize Task 2',
 'original20gap':'original 20 gap','OnlyF05':'Only F05','andB06':'and B06',
 'All93material':'All 93 material','these93claim-units':'these 93 claim-units',
 'original3contradicted':'original 3 contradicted','eightMEDIUM':'eight MEDIUM',
 'oneHIGH,fiveMEDIUM,twoLOW':'one HIGH, five MEDIUM, two LOW',
 'All11 proposals':'All 11 proposals','Eightfindings':'Eight findings',
 'oneHIGH,fiveMEDIUM':'one HIGH, five MEDIUM','twoLOW':'two LOW',
 'SEC-01and':'SEC-01 and','51literal':'51 literal','67strictindexmatches52collectionmetadata':'67 strict index matches in 52-collection metadata',
 '52savedcollectionflags':'52 saved collection flags','old8150baseline':'old 8,150 baseline',
 'Prior8476baseline':'Prior 8,476 baseline','current8504baseline':'current 8,504 baseline',
 '8150baseline':'8,150 baseline','8476baseline':'8,476 baseline','8504baseline':'8,504 baseline',
 '13required':'13 required','original8150set':'original 8,150 set',
 '39currentXMLhashes':'39 current XML hashes','all39':'all 39','all13':'all 13',
 'current/production':'current / production','notTest':'not Test',
 'sourceguards':'source guards','sourcepatterns':'source patterns',
 'All179explicit':'All 179 explicit','60BaseModel':'60 BaseModel',
 'Only4endpoints':'Only 4 endpoints','27Queryparameters':'27 Query parameters',
 'across19endpoints':'across 19 endpoints','387signature':'387 signature',
 '216with':'216 with','Sixty model':'Sixty model','60does':'60 does','mean60HTTP':'mean 60 HTTP',
 '19endpoints':'19 endpoints','95TS/TSX':'95 TS/TSX','53app':'53 app',
 'The579event':'The 579 event','not579working':'not 579 working','The108 previously':'The 108 previously',
 '107unconditional':'107 unconditional','6leaves':'6 leaves','3two-branch':'3 two-branch',
 '113literal':'113 literal','old108set':'old 108 set','Original108checks':'Original 108 checks',
 '12entity-template':'12 entity-template','threeMEDIUM':'three MEDIUM',
 '67declarations':'67 declarations','81GET':'81 GET','remaining78are':'remaining 78 are',
 'sourceURL':'source URL','metadataJSON':'metadata JSON','rawhello':'raw hello',
 '52saved':'52 saved','read_only_current':'read_only_current',
}
opaque=re.compile(r'(\[[^\]\n]+\]\(<[^>\n]+>\)|`[^`\n]*`)')
for p in here.glob('FINAL_*.md'):
    out=[]
    fenced=False
    for line in p.read_text().splitlines(keepends=True):
        if line.startswith('```'):
            fenced=not fenced
            out.append(line)
            continue
        if fenced:
            out.append(line)
            continue
        parts=opaque.split(line)
        for i in range(0,len(parts),2):
            for before,after in replacements.items():
                parts[i]=parts[i].replace(before,after)
        out.append(''.join(parts))
    p.write_text(''.join(out))
print('Spaced prose in five NEW iteration reports only;code fences,inline code and link targets preserved.')
