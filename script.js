// ============================================
// KOS BERKAH GUNUNGKIDUL - MAIN SCRIPT
// ============================================

// --- Page Navigation ---
function showPage(pageName) {
  // Hide all pages
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  // Show target page
  const target = document.getElementById('page-' + pageName);
  if (target) {
    target.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Update nav active state
  document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
  if (pageName === 'home') {
    document.getElementById('navHome').classList.add('active');
  } else if (pageName === 'rules') {
    document.getElementById('navRules').classList.add('active');
  }

  // Close mobile menu
  document.getElementById('navLinks').classList.remove('open');
}

// --- Scroll To Section ---
function scrollToSection(id) {
  const el = document.getElementById(id);
  if (el) {
    const offset = 80;
    const top = el.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });
  }
}

// --- Navbar Scroll Effect ---
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 30) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});

// --- Mobile Nav Toggle ---
const navToggle = document.getElementById('navToggle');
const navLinks  = document.getElementById('navLinks');

navToggle.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});

// Close mobile nav on link click
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
  });
});

// --- Intersection Observer: Animate on Scroll ---
const observerOptions = {
  threshold: 0.12,
  rootMargin: '0px 0px -60px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

function initAnimations() {
  const animatables = document.querySelectorAll(
    '.feature-card, .gallery-item, .address-card, .contact-card, .rules-block'
  );

  animatables.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = `opacity 0.6s ease ${i * 0.07}s, transform 0.6s ease ${i * 0.07}s`;
    observer.observe(el);
  });
}

// Re-init when page changes
const pageObserver = new MutationObserver(() => {
  initAnimations();
});
pageObserver.observe(document.body, { subtree: true, attributes: true, attributeFilter: ['class'] });

// Init on load
document.addEventListener('DOMContentLoaded', () => {
  initAnimations();
});
