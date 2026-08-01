import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Insert nav link
nav_link = '        <a href="#" class="nav-link" id="navContact" onclick="showPage(\'contact\')">Info & Kontak</a>'
content = content.replace(
    '        <a href="#" class="nav-link" id="navRules" onclick="showPage(\'rules\')">Tata Tertib</a>',
    '        <a href="#" class="nav-link" id="navRules" onclick="showPage(\'rules\')">Tata Tertib</a>\n' + nav_link
)

# 2. Insert page contact
page_contact_html = """
  <!-- ============================== -->
  <!-- PAGE 3: INFO & KONTAK          -->
  <!-- ============================== -->
  <div id="page-contact" class="page">
    <section class="rules-hero contact-hero">
      <div class="rules-hero-content">
        <div class="rules-hero-icon">
          <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>
        </div>
        <h1>Info & Kontak</h1>
        <p>Kos Berkah Gunungkidul</p>
        <div class="rules-hero-desc">
          Akses cepat untuk membagikan alamat, lokasi, atau menghubungi kami.
        </div>
      </div>
    </section>

    <section class="contact-section">
      <div class="container contact-container">
        
        <!-- Akses Cepat / Copy -->
        <div class="contact-grid">
          
          <div class="copy-card">
            <div class="copy-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg></div>
            <h3>Alamat Lengkap</h3>
            <p>Siyono Tengah RT 41 RW 07, Logandeng, Playen, Gunungkidul</p>
            <button class="btn-copy" onclick="copyTextToClipboard('Siyono Tengah RT 41 RW 07, Logandeng, Playen, Gunungkidul')">Salin Alamat</button>
          </div>

          <div class="copy-card">
            <div class="copy-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"/><line x1="9" y1="3" x2="9" y2="18"/><line x1="15" y1="6" x2="15" y2="21"/></svg></div>
            <h3>Link Google Maps</h3>
            <p>Bagikan lokasi via Maps</p>
            <button class="btn-copy" onclick="copyTextToClipboard('https://www.google.com/maps?q=-7.96662,110.60205')">Salin Link Maps</button>
          </div>

          <div class="copy-card">
            <div class="copy-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg></div>
            <h3>Nomor WhatsApp</h3>
            <p>085924695164</p>
            <button class="btn-copy" onclick="copyTextToClipboard('085924695164')">Salin Nomor</button>
          </div>

          <div class="copy-card">
            <div class="copy-card-icon"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg></div>
            <h3>Format Chat</h3>
            <p>Template tanya kamar kosong</p>
            <button class="btn-copy" onclick="copyTextToClipboard('Halo, saya dapat info dari website Kos Berkah. Apakah masih ada kamar kosong untuk bulan ini?')">Salin Format</button>
          </div>
          
        </div>

        <div class="contact-extras">
          
          <!-- QR Code Section -->
          <div class="qr-section">
            <h3>Scan QR WhatsApp</h3>
            <div class="qr-box">
              <img src="qrwa.png" alt="QR Code WhatsApp Kos Berkah" />
            </div>
            <p>Scan untuk langsung menghubungi pemilik</p>
          </div>

          <!-- Emergency Numbers -->
          <div class="emergency-section">
            <h3>Nomor Darurat Gunungkidul</h3>
            <ul class="emergency-list">
              <li><span>Layanan Darurat Terpadu</span><strong>112</strong></li>
              <li><span>RSUD Wonosari</span><strong>(0274) 391007</strong></li>
              <li><span>Polres Gunungkidul</span><strong>(0274) 391110</strong></li>
              <li><span>Pemadam Kebakaran</span><strong>(0274) 391113</strong></li>
            </ul>
          </div>
        </div>

      </div>
    </section>
    
    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-brand">
            <img src="logo.jpg" alt="Logo Kos Berkah" class="footer-logo" />
            <span>Kos Berkah Gunungkidul</span>
          </div>
          <p class="footer-tagline">Hunian nyaman, hati tenang</p>
          <p class="footer-copy">&copy; 2026 Kos Berkah Gunungkidul. All Right Reserved.</p>
        </div>
      </div>
    </footer>
  </div>
"""

content = content.replace('  </div><!-- end page-rules -->', '  </div><!-- end page-rules -->\n' + page_contact_html)

# Add a toast div to body for notifications
toast_html = '\n  <div id="toast" class="toast">Berhasil disalin!</div>\n</body>'
content = content.replace('</body>', toast_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Insertion done.")
