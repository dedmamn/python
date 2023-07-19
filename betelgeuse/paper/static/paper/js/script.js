cardsinds = [6, 5, 4, 3, 2, 1];

    function test(card_id){
      cards = [];
      cards[1] = document.querySelector('.card1');
      cards[2] = document.querySelector('.card2');
      cards[3] = document.querySelector('.card3');
      cards[4] = document.querySelector('.card4');
      cards[5] = document.querySelector('.card5');
      cards[6] = document.querySelector('.card6');

      

      if (card_id == 1){
        cards[1].style.zIndex = 6;
        cards[2].style.zIndex = 5;
        cards[3].style.zIndex = 4;
        cards[4].style.zIndex = 3;
        cards[5].style.zIndex = 2;
        cards[6].style.zIndex = 1;

        cards[1].style.backgroundColor = "#ffffff";
        cards[2].style.backgroundColor = "#D3D3D3";
        cards[3].style.backgroundColor = "#D3D3D3";
        cards[4].style.backgroundColor = "#D3D3D3";
        cards[5].style.backgroundColor = "#D3D3D3";
        cards[6].style.backgroundColor = "#D3D3D3";
      }
      if (card_id == 2){
        cards[1].style.zIndex = 5;
        cards[2].style.zIndex = 6;
        cards[3].style.zIndex = 4;
        cards[4].style.zIndex = 3;
        cards[5].style.zIndex = 2;
        cards[6].style.zIndex = 1;
        cards[1].style.backgroundColor = "#D3D3D3";
        cards[2].style.backgroundColor = "#ffffff";
        cards[3].style.backgroundColor = "#D3D3D3";
        cards[4].style.backgroundColor = "#D3D3D3";
        cards[5].style.backgroundColor = "#D3D3D3";
        cards[6].style.backgroundColor = "#D3D3D3";
      }
      if (card_id == 3){
        cards[1].style.zIndex = 4;
        cards[2].style.zIndex = 5;
        cards[3].style.zIndex = 6;
        cards[4].style.zIndex = 3;
        cards[5].style.zIndex = 2;
        cards[6].style.zIndex = 1;
        cards[1].style.backgroundColor = "#D3D3D3";
        cards[2].style.backgroundColor = "#D3D3D3";
        cards[3].style.backgroundColor = "#ffffff";
        cards[4].style.backgroundColor = "#D3D3D3";
        cards[5].style.backgroundColor = "#D3D3D3";
        cards[6].style.backgroundColor = "#D3D3D3";
      }
      if (card_id == 4){
        cards[1].style.zIndex = 3;
        cards[2].style.zIndex = 4;
        cards[3].style.zIndex = 5;
        cards[4].style.zIndex = 6;
        cards[5].style.zIndex = 2;
        cards[6].style.zIndex = 1;
        cards[1].style.backgroundColor = "#D3D3D3";
        cards[2].style.backgroundColor = "#D3D3D3";
        cards[3].style.backgroundColor = "#D3D3D3";
        cards[4].style.backgroundColor = "#ffffff";
        cards[5].style.backgroundColor = "#D3D3D3";
        cards[6].style.backgroundColor = "#D3D3D3";
      }
      if (card_id == 5){
        cards[1].style.zIndex = 2;
        cards[2].style.zIndex = 3;
        cards[3].style.zIndex = 4;
        cards[4].style.zIndex = 5;
        cards[5].style.zIndex = 6;
        cards[6].style.zIndex = 1;
        cards[1].style.backgroundColor = "#D3D3D3";
        cards[2].style.backgroundColor = "#D3D3D3";
        cards[3].style.backgroundColor = "#D3D3D3";
        cards[4].style.backgroundColor = "#D3D3D3";
        cards[5].style.backgroundColor = "#ffffff";
        cards[6].style.backgroundColor = "#D3D3D3";
      }
      if (card_id == 6){
        cards[1].style.zIndex = 1;
        cards[2].style.zIndex = 2;
        cards[3].style.zIndex = 3;
        cards[4].style.zIndex = 4;
        cards[5].style.zIndex = 5;
        cards[6].style.zIndex = 6;
        cards[1].style.backgroundColor = "#D3D3D3";
        cards[2].style.backgroundColor = "#D3D3D3";
        cards[3].style.backgroundColor = "#D3D3D3";
        cards[4].style.backgroundColor = "#D3D3D3";
        cards[5].style.backgroundColor = "#D3D3D3";
        cards[6].style.backgroundColor = "#ffffff";
      }
    }

    function hideCards(start, end) {
  for (let i = parseInt(start.slice(4)); i <= parseInt(end.slice(4)); i++) {
    const card = document.querySelector('.card' + i);
    if (card) {
      card.style.zIndex = cardsinds[i];
      // card.dataset.previousZIndex = card.style.zIndex; // Store the previous z-index value
      card.style.display = 'none';
    }
  }
}

    function showCard(card) {
      const cardElement = document.querySelector('.' + card);
      if (cardElement) {
        cardElement.style.display = 'grid';
      }
    }
