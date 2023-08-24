/* ------------main.js 2-------------*/
/*--------limit the number of characters in the paragraph for healthtips*/
document.addEventListener('DOMContentLoaded', 
function () {
      const paragraphs = document.getElementsByClassName('description');

      for (let i = 0; i < paragraphs.length; i++) {
        const inputText = paragraphs[i].textContent;
        const limit = 300;
        const end = ' .....Click on heading to read.....';
        if (inputText.length > limit) {
            paragraphs[i].textContent = inputText.substring(0, limit) + end;
          }
          
        }
      
    });

    /*---------the blog page(all healthtips page)---------*/
document.addEventListener('DOMContentLoaded', 
function () {
        const paragraphs = document.getElementsByClassName('blog-description');

        for (let i = 0; i < paragraphs.length; i++) {
        const inputText = paragraphs[i].textContent;
        const limit = 100;
        const end = ' .....';
        if (inputText.length > limit) {
            paragraphs[i].textContent = inputText.substring(0, limit) + end;
            }
            
        }
        
    });  
    
 /**
   * Whatsapp button
   */
 let backtotop = select('.whatsapp')
 if (backtotop) {
   const toggleBacktotop = () => {
     if (window.scrollY > 100) {
       backtotop.classList.add('active')
     } else {
       backtotop.classList.remove('active')
     }
   }
   window.addEventListener('load', toggleBacktotop)
   onscroll(document, toggleBacktotop)
 }    
