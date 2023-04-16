
$(document).ready(function() {
    // Hide all images initially
    $('.hidden').hide();
  
    // Show the image corresponding to the clicked menu item
    $('a').click(function() {
      var imageSelector = $(this).data('image');
      $(imageSelector).toggle();
    });
  });




