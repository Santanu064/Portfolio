
function ReloadAnimation(Selector, ClassName) {
  const elementsToAnimate = document.querySelectorAll(Selector);
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add(ClassName);
      } else {
        entry.target.classList.remove(ClassName);
      }
    });
  });

  elementsToAnimate.forEach((element) => {
    observer.observe(element);
  });
}

ReloadAnimation('.animate-on-scroll', 'animate-on-scroll');
ReloadAnimation('.curve-animation','curve-animation')