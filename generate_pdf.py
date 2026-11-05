import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (Pages 2+)
        if self._pageNumber > 1:
            self.drawString(54, 750, "CloakHer (AegisPix) — IEEE WIE Artemia 2.0 Ideathon Proposal")
            self.setStrokeColor(colors.HexColor("#e2e8f0"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
            
        # Footer
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 36, page_str)
        self.drawString(54, 36, "Confidential — For Artemia 2.0 Evaluation & Team Internal Reference")
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)
        self.restoreState()

def build_pdf(filename="D:/idea_mart/CloakHer_Project_Proposal.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#4f46e5'),
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1e1b4b'),
        spaceBefore=14,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#312e81'),
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=6
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    quote_style = ParagraphStyle(
        'QuoteText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=14,
        textColor=colors.HexColor('#3730a3')
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#0f172a')
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#334155')
    )

    story = []

    # Title Banner
    story.append(Paragraph("CloakHer (AegisPix)", title_style))
    story.append(Paragraph("Adversarial Immunization & Invisible Steganographic Shield for Women's Social Imagery", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor('#6366f1'), spaceAfter=12))

    # Meta Info Table
    meta_data = [
        [
            Paragraph("<b>Competition:</b> Artemia 2.0 (IEEE WIE USJ)", table_cell),
            Paragraph("<b>Theme:</b> Women's Safety & Cyber Defense", table_cell),
            Paragraph("<b>Aligned Goals:</b> UN SDGs 5, 9, 11", table_cell)
        ],
        [
            Paragraph("<b>Track:</b> Ideathon & Designathon", table_cell),
            Paragraph("<b>Platform:</b> Web & Mobile Application", table_cell),
            Paragraph("<b>Core Tech:</b> Agentic AI + Adversarial ML", table_cell)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[170, 170, 164])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # 1. Executive Summary
    story.append(Paragraph("1. Executive Summary", h1_style))
    story.append(Paragraph(
        "<b>CloakHer</b> is an autonomous protective ecosystem that solves digital sexual harassment, "
        "non-consensual deepfake generation, and cyber-blackmail targeting women. Rather than offering a reactive panic button "
        "that triggers only after abuse occurs, CloakHer <b>immunizes personal photographs before they are posted online</b>. "
        "By injecting imperceptible adversarial perturbations and frequency-domain cryptographic marks, the photo remains completely "
        "natural to human eyes while rendering itself unprocessable and mathematically disruptive to generative AI models and illicit nudify algorithms.",
        body_style
    ))

    # 2. Problem Statement (Session 01 Standard)
    story.append(Paragraph("2. Problem Identification & Prioritization", h1_style))
    story.append(Paragraph(
        "In accordance with Artemia 2.0 Session 01 guidelines (<i>'Stay in the problem space — describing your app here is the #1 mistake'</i>), "
        "the core problem is defined strictly around human vulnerability and tangible consequences:",
        body_style
    ))

    prob_statement_html = (
        "<b>Validated Problem Statement:</b><br/>"
        "Young women and female university students active on social media (<b>Who</b>) struggle with the unauthorized scraping and "
        "weaponization of their personal photographs into AI-generated non-consensual intimate imagery and blackmail material (<b>What</b>) "
        "because publicly shared photographs have zero built-in technical defense against generative diffusion models and victims possess "
        "no instantaneous method to legally prove synthetic tampering (<b>Why</b>), leading to severe psychological trauma, social stigmatization, "
        "reputational extortion, academic derailment, and forced withdrawal from digital society (<b>Consequence</b>)."
    )
    
    quote_table = Table([[Paragraph(prob_statement_html, quote_style)]], colWidths=[504])
    quote_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f5f3ff')),
        ('LINELEFT', (0,0), (-1,-1), 4, colors.HexColor('#7c3aed')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#ddd6fe')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(quote_table)
    story.append(Spacer(1, 8))

    # 3. Technical Architecture
    story.append(Paragraph("3. Technical Architecture: 3-Layer Defense Engine", h1_style))
    story.append(Paragraph(
        "To withstand rigorous technical critique, CloakHer abandons fragile visible watermarks (which can be easily cropped or in-painted) "
        "in favor of a robust mathematical three-layer defense:",
        body_style
    ))

    layers_data = [
        [
            Paragraph("<b>Layer</b>", table_header),
            Paragraph("<b>Methodology</b>", table_header),
            Paragraph("<b>Mechanism & Threat Neutralization</b>", table_header)
        ],
        [
            Paragraph("<b>Layer 1:<br/>Adversarial Cloaking</b>", table_cell),
            Paragraph("Targeted Latent Perturbation (PGD/FGSM)", table_cell),
            Paragraph("Injects microscopic changes (&plusmn;1-2 RGB) across facial contours. When ingested by diffusion models, the noise induces mathematical collapse in the latent space, outputting broken, distorted blurs.", table_cell)
        ],
        [
            Paragraph("<b>Layer 2:<br/>Provenance Signature</b>", table_cell),
            Paragraph("DWT-DCT Steganography + C2PA Standard", table_cell),
            Paragraph("Embeds tamper-resilient frequency metadata. Survives compression and screenshots. Compliant commercial AI APIs (OpenAI, Midjourney, Adobe) detect the 'Protected Identity' flag and abort generation.", table_cell)
        ],
        [
            Paragraph("<b>Layer 3:<br/>Forensic Verification</b>", table_cell),
            Paragraph("Zero-Knowledge Perceptual Hashing (pHash)", table_cell),
            Paragraph("Computes one-way perceptual hashes without storing private user photos. If extortion occurs, the user verifies suspicious media and exports an automated, legally formatted Sri Lanka CERT complaint dossier.", table_cell)
        ]
    ]
    layers_table = Table(layers_data, colWidths=[105, 125, 274])
    layers_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e0e7ff')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(layers_table)

    story.append(PageBreak())

    # 4. Agentic AI Integration
    story.append(Paragraph("4. Agentic AI Integration (Session 02 Alignment)", h1_style))
    story.append(Paragraph(
        "Directly translating the workshop framework (Conducted by Ravindu Jayaweera) into production capability, "
        "CloakHer operates via an autonomous <b>Plan &rarr; Act &rarr; Observe &rarr; Decide</b> loop with explicit guardrails:",
        body_style
    ))

    agent_data = [
        [Paragraph("<b>Step</b>", table_header), Paragraph("<b>Agent Role</b>", table_header), Paragraph("<b>Technical Operation</b>", table_header)],
        [Paragraph("<b>1. PLAN</b>", table_cell), Paragraph("Vulnerability & Landmark Analysis", table_cell), Paragraph("Scans facial landmarks, skin tones, and background to formulate the optimal minimal perturbation matrix.", table_cell)],
        [Paragraph("<b>2. ACT</b>", table_cell), Paragraph("Tensor Perturbation & Provenance", table_cell), Paragraph("Applies adversarial pixel perturbations and injects DWT frequency-domain digital signatures.", table_cell)],
        [Paragraph("<b>3. OBSERVE</b>", table_cell), Paragraph("Autonomous Self-Evaluation", table_cell), Paragraph("Attempts to execute an automated internal diffusion reconstruction on the newly cloaked asset to test defense integrity.", table_cell)],
        [Paragraph("<b>4. DECIDE</b>", table_cell), Paragraph("Convergence & Release", table_cell), Paragraph("Loops back to calibrate strength if reconstruction succeeds; releases the protected file once immunization exceeds 95%.", table_cell)]
    ]
    agent_table = Table(agent_data, colWidths=[65, 140, 299])
    agent_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(agent_table)
    story.append(Spacer(1, 8))

    # Guardrails Callout
    guardrails_html = (
        "<b>Responsible Autonomy & Safety Guardrails (Session 02 Compliance):</b><br/>"
        "• <b>Zero-Storage Blast Radius Limitation:</b> Uncloaked photographs are processed exclusively within volatile RAM and deleted immediately after tensor perturbation.<br/>"
        "• <b>Human-in-the-Loop Authority:</b> The system will never transmit automated complaints to law enforcement or CERT without explicit manual confirmation by the user."
    )
    guard_table = Table([[Paragraph(guardrails_html, table_cell)]], colWidths=[504])
    guard_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f0fdf4')),
        ('LINELEFT', (0,0), (-1,-1), 4, colors.HexColor('#16a34a')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#bbf7d0')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(guard_table)
    story.append(Spacer(1, 10))

    # 5. Project Scope & MoSCoW Prioritization
    story.append(Paragraph("5. Project Scope & Prioritization (Session 01 Standard)", h1_style))
    story.append(Paragraph(
        "Applying the strict <i>'Maximum 3 MUST features'</i> mandate to ensure 100% buildability by Phase 03:",
        body_style
    ))

    scope_data = [
        [Paragraph("<b>Category</b>", table_header), Paragraph("<b>Feature Module</b>", table_header), Paragraph("<b>Scope & Deliverable</b>", table_header)],
        [Paragraph("<font color='#16a34a'><b>MUST 1</b></font>", table_cell), Paragraph("One-Click Photo Immunization", table_cell), Paragraph("Upload interface injecting invisible adversarial cloak + invisible watermarking. Instant export.", table_cell)],
        [Paragraph("<font color='#16a34a'><b>MUST 2</b></font>", table_cell), Paragraph("AI Attack Simulator", table_cell), Paragraph("Interactive UI component demonstrating side-by-side how an AI generator fails on the cloaked image.", table_cell)],
        [Paragraph("<font color='#16a34a'><b>MUST 3</b></font>", table_cell), Paragraph("Forensic Tampering Verifier", table_cell), Paragraph("Upload tool for suspected deepfakes that verifies authenticity and compiles a ready-to-file CERT report.", table_cell)],
        [Paragraph("<font color='#2563eb'><b>SHOULD</b></font>", table_cell), Paragraph("Social Media Exposure Audit", table_cell), Paragraph("Guidance scanner evaluating public profile vulnerability to automated scraping.", table_cell)],
        [Paragraph("<font color='#9333ea'><b>COULD</b></font>", table_cell), Paragraph("Browser Protection Extension", table_cell), Paragraph("Right-click context menu wrapper for instant desktop protection prior to upload.", table_cell)],
        [Paragraph("<font color='#64748b'><b>NOT YET</b></font>", table_cell), Paragraph("Live Video Frame Perturbation", table_cell), Paragraph("Real-time webcam adversarial injection for streaming platforms (Deferred to future roadmap).", table_cell)]
    ]
    scope_table = Table(scope_data, colWidths=[80, 150, 274])
    scope_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(scope_table)
    story.append(Spacer(1, 10))

    # 6. Competition Roadmap & Live Demo Strategy
    story.append(Paragraph("6. Competition Roadmap & Evaluation Edge", h1_style))
    story.append(Paragraph(
        "• <b>Phase 01 (Ideathon):</b> Submission of comprehensive problem statement, architecture diagrams, and value proposition canvas.<br/>"
        "• <b>Phase 02 (Designathon):</b> High-fidelity Figma prototype showcasing the 'One-Click Cloaking Experience', 'AI Simulator', and 'Forensic Triage Portal'.<br/>"
        "• <b>Phase 03 (Final Live Pitch):</b> <b>The Showstopper Stage Demo:</b> On stage, the team presents two identical-looking photos of a female teammate. "
        "Feeding the unprotected photo into a generative AI tool shows instant face alteration. Feeding the CloakHer-immunized photo causes the exact same AI engine "
        "to fail catastrophically and return a glitched blur live in front of the judges.",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF successfully generated.")

if __name__ == "__main__":
    build_pdf()
