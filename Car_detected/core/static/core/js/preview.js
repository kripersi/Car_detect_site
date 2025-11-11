document.addEventListener("DOMContentLoaded", function() {
  const fileInputs = document.querySelectorAll('input[type="file"]');

  fileInputs.forEach(input => {
    const previewContainer = document.createElement("div");
    previewContainer.classList.add("image-preview-container");
    input.insertAdjacentElement("afterend", previewContainer);

    input.addEventListener("change", function(event) {
      const files = event.target.files;
      previewContainer.innerHTML = "";

      if (files && files.length > 0) {
        Array.from(files).forEach(file => {
          const reader = new FileReader();
          reader.onload = function(e) {
            const img = document.createElement("img");
            img.src = e.target.result;
            img.classList.add("preview-image");
            previewContainer.appendChild(img);
          };
          reader.readAsDataURL(file);
        });
      }
    });
  });
});
