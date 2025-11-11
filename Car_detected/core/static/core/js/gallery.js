document.addEventListener("DOMContentLoaded", () => {
  const track = document.querySelector(".photo-track");
  const photos = document.querySelectorAll(".gallery-photo");
  const prevBtn = document.querySelector(".prev-btn");
  const nextBtn = document.querySelector(".next-btn");

  if (!track || photos.length === 0) return;

  let index = 0;

  function showImage(i) {
    index = (i + photos.length) % photos.length;
    const offset = -index * 100;
    track.style.transform = `translateX(${offset}%)`;
  }

  nextBtn.addEventListener("click", () => {
    showImage(index + 1);
  });

  prevBtn.addEventListener("click", () => {
    showImage(index - 1);
  });
});
