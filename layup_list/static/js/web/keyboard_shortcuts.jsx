LayupList.Web.KeyboardShortcuts = function() {
    
    // cmd k to focus search bar
    $(document).on('keydown', function(e) {
        if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
            e.preventDefault();
            
            var searchInput = $('#navbar-search');
            if (searchInput.length) {
                searchInput.focus();
                searchInput.select();
            }
        }
    });
    
};
