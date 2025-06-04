from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    summary = request.form["summary"]

    # Create PDF in memory
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, 750, f"Resume - {name}")

    c.setFont("Helvetica", 14)
    c.drawString(50, 700, "Professional Summary:")
    textobject = c.beginText(50, 680)
    textobject.setFont("Helvetica", 12)
    for line in summary.split("\n"):
        textobject.textLine(line)
    c.drawText(textobject)

    c.showPage()
    c.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name=f"{name}_Resume.pdf", mimetype='application/pdf')

if __name__ == "__main__":
    app.run(debug=True)
