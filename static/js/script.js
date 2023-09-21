
//PICTURE 1
    const inputFile = document.getElementById("picture__input");
    const picturePreview = document.getElementById("picture__preview");
    const pictureImageTxt = "Choose an image";

    // Dodajte event listener za klik na labelu kako biste otvorili input polje
    document.querySelector(".picture").addEventListener("click", () => {
      inputFile.click();
    });

    inputFile.addEventListener("change", function (e) {
      const inputTarget = e.target;
      const file = inputTarget.files[0];
  
      if (file) {
        const reader = new FileReader();
  
        reader.addEventListener("load", function (e) {
          const readerTarget = e.target;
  
          const img = document.createElement("img");
          img.src = readerTarget.result;
          img.classList.add("picture__img");
  
          picturePreview.innerHTML = "";
          picturePreview.appendChild(img);
        });
  
        reader.readAsDataURL(file);
      } else {
        picturePreview.innerHTML = pictureImageTxt;
      }
    });

//DROPDOWN MENU
        const dropdowns=document.querySelectorAll('.dropdown')
        //Loop through all drop down elements
        dropdowns.forEach(dropdown =>{
            //Get inner elemets from each dropdown
            const select = dropdown.querySelector('.select');
            const caret = dropdown.querySelector('.caret');
            const menu = dropdown.querySelector('.menu');
            const options = dropdown.querySelectorAll('.menu li');
            const selected = dropdown.querySelector('.selected');
        //Add a click event to the select elemenet
        select.addEventListener('click', () => {
            //Add the clicked select styles to the select element
            select.classList.toggle('select-clicked');
            //Add the rotate styles to the caret elemet
            caret.classList.toggle('caret-rotate');
            //Add the open styles to the menu element
            menu.classList.toggle('menu-open');
        });
        //Loop throuh all option elements
        options.forEach(option =>{
            //Add a click event to the option element
            option.addEventListener('click', () =>{
                //Change selected inner text to clicked option inner text
                selected.innerText = option.innerText;
                //Add the clicked slect styles to the select element
                select.classList.remove('select-clicked'); 
                //Add the rotate styles to thge caret element
                caret.classList.remove('caret-rotate');
                //Add the open styles to the menu element
                menu.classList.remove('menu-open');
                //Remove active class from all option elements
                options.forEach(option => {
                    option.classList.remove('active');
                });
                //Add active class to clicked option element
                option.classList.add('active');
                });
            });
        });




