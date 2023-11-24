$( document ).ready(function() {
    var boards = $('.travel-type');
    var current_idx = 1;
    var counter = 0;

    setInterval(rotate, 10000)
    console.log(current_idx)

    function rotate() {
        console.log('rotating')

        if(counter === 10) {
            location.reload();
        }

        for(i=0; i< boards.length; i++) {
            if(i !== current_idx) {
                $(boards[i]).hide();
            }else {
                $(boards[i]).show();
            }
        }

        current_idx = current_idx + 1 === boards.length ? 0 : current_idx + 1
        counter ++;
    }
});