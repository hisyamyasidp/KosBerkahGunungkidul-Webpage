// ============================================
// KOS BERKAH GUNUNGKIDUL - MAIN SCRIPT
// ============================================

// --- Page Navigation ---
function showPage(pageName) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  const target = document.getElementById('page-' + pageName);
  if (target) {
    target.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
    // Trigger animations for newly visible page
    setTimeout(() => observeElements(target), 50);
  }

  document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
  if (pageName === 'home')  document.getElementById('navHome').classList.add('active');
  if (pageName === 'rules') document.getElementById('navRules').classList.add('active');
  if (pageName === 'contact') document.getElementById('navContact').classList.add('active');

  document.getElementById('navLinks').classList.remove('open');
  document.getElementById('navToggle').classList.remove('active');
}

// --- Scroll To Section ---
function scrollToSection(id) {
  const el = document.getElementById(id);
  if (el) {
    const top = el.getBoundingClientRect().top + window.scrollY - 80;
    window.scrollTo({ top, behavior: 'smooth' });
  }
}

// --- Navbar Scroll Effect ---
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 30);
});

// --- Mobile Nav Toggle ---
const navToggle = document.getElementById('navToggle');
const navLinks  = document.getElementById('navLinks');

navToggle.addEventListener('click', () => {
  navLinks.classList.toggle('open');
  navToggle.classList.toggle('active');
});

document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    navToggle.classList.remove('active');
  });
});

// --- Intersection Observer: Animate on Scroll ---
const SELECTORS = '.feature-card, .gallery-item, .address-card, .contact-card, .rules-block';

// Track observed elements to avoid double-init
const observed = new WeakSet();

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry, idx) => {
    if (entry.isIntersecting) {
      const el = entry.target;
      // Small staggered delay based on position within its siblings
      const siblings = Array.from(el.parentElement.children).filter(c => c.matches && c.matches(SELECTORS));
      const pos = siblings.indexOf(el);
      const delay = Math.min(pos * 60, 240); // max 240ms total stagger
      setTimeout(() => {
        el.style.opacity = '1';
        el.style.transform = 'translateY(0)';
      }, delay);
      observer.unobserve(el);
    }
  });
}, {
  threshold: 0.05,          // trigger earlier
  rootMargin: '0px 0px 0px 0px'
});

function observeElements(root) {
  const els = (root || document).querySelectorAll(SELECTORS);
  els.forEach(el => {
    if (observed.has(el)) return; // skip already-processed
    observed.add(el);
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.35s ease, transform 0.35s ease';
    observer.observe(el);
  });
}

// Init on load
document.addEventListener('DOMContentLoaded', () => {
  observeElements(document.getElementById('page-home'));
});

// --- Copy to Clipboard ---
function copyTextToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    showToast("Teks berhasil disalin!");
  }).catch(err => {
    console.error('Failed to copy: ', err);
    showToast("Gagal menyalin teks.");
  });
}

function copyWithFeedback(btn, text) {
  navigator.clipboard.writeText(text).then(() => {
    btn.classList.add('copied');
    showToast("Berhasil disalin!");
    setTimeout(() => btn.classList.remove('copied'), 2000);
  }).catch(() => {
    showToast("Gagal menyalin.");
  });
}

function showToast(message) {
  const toast = document.getElementById("toast");
  if (!toast) return;
  toast.innerText = message;
  toast.className = "toast show";
  setTimeout(() => {
    toast.className = toast.className.replace("show", "");
  }, 3000);
}
