
from flask import Flask, render_template, abort
from flask_googlemaps import GoogleMaps
app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = "AIzaSyA-9AdZL7MFnR0_-ymCG_ImFZBKStnHBnk"

class ADHC:
    def __init__(self,key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

ADHCS = (
    ADHC('A plus', 'A Plus Adult Day Health Care',   34.069279, -118.0346144),
    ADHC('Ararat','Ararat Adult Day Health Care Center',  34.138409, -118.251629),
    ADHC('Arcadia','Arcadia Adult Day Health Care Center', 34.140164, -117.995246),
    ADHC('Beverly','Beverly Adult Day Health Care Center' ,34.077102,-118.309076 ),
    ADHC('Burbank ','Burbank Adult Day Health Care Center ',34.178613,-118.34004),
    ADHC('C & C','C & C Carson Adult Day Health Care Center',33.847448,-118.266162),
    ADHC('E & V','E & V Adult Day Health Care Center',33.91126,-118.239426),
    ADHC('F & F','F & F Adult Day Health Care Center',33.800782,-118.193971),
    ADHC('Forever Young','Forever Young Adult Day Health Care Center',34.090174,-117.960604),
    ADHC( 'Glen1','Glendale Gardens Adult Day Health Care Center',34.1442611,-118.2498299),
    ADHC('Glen2 ', 'Glendale Hills Adult Day Health Care Center',34.1545337,-118.2424748),
    ADHC('HL', 'HealthyLife Adult Day Health Care', 34.000182,-118.4173852),
    ADHC('Home Ave','Home Avenue Adult Day Health Care Center',33.9675561,-118.1169067),
    ADHC('Sunrise','New Sunrise Adult Day Health Care Center',34.2406608,-118.535558),
    ADHC('Onegen','ONEgeneration Adult Day Healthcare Center',34.185708,-118.5132304),
    ADHC('SC','Santa Clarita Adult Day Healthcare Center',34.0770982,-118.0903667),
    ADHC('SW','Silver Wisdom Adult Day Health Care Center',34.1023091,-118.3276064),
    ADHC('Sunnycal','Sunny Cal Adult Day Health Care Center',34.0799853,-118.0850167),
    ADHC('Suunyday','SunnyDay Adult Day Health Care Center',34.091603,-118.0390205),
    ADHC('Universal','Universal Adult Day Health Care Center',34.0035164,-118.430412),
    ADHC('Valley','Valley Village Adult Day Health Care',34.2014478,-118.5876368),
    ADHC('victory','Victory Adult Day Health Center',34.1623419,-118.3016085),
    ADHC('W&F','Well and Fit Adult Day Health Care Center',34.0565977,-117.8024749),
    ADHC('Wellcare','Wellcare Adult Day Health Care Center',34.1932007,-118.4569586)
)

ADHCS_by_key = {ADHC.key: ADHC for ADHC in ADHCS }

@app.route("/")
def index():
    return render_template('index.html', ADHCS= ADHCS )

@app.route("/<ADHC_code>")
def show_ADHC(ADHC_code):
   ADHC  = ADHCS_by_key.get(ADHC_code)
   if ADHC:
        return render_template('GMAP.html', ADHC=ADHC)
   else:
        abort(404)

app.run(host="localhost", port=8000, debug=True)