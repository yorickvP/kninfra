(function(){
  function KNF(){
    this.fotos_request_count = 12;
  }

  KNF.prototype.change_path = function(path) {
    $('#fotos').empty();
    this.path = path;
    this.fotos_offset = 0;
    this.fetched_all_fotos = false;
    this.fetching_more_fotos = false;
    this.fetch_more_fotos();
  };

  KNF.prototype.fetch_more_fotos = function() {
    var that = this;
    this.fetching_more_fotos = true;
    var old_path = this.path;
    this.api({action: 'list',
              path: this.path,
              offset: this.fotos_offset,
              count: this.fotos_request_count},
      function(data) {
        if(old_path != that.path) return;
        if(data.error) return alert(data.error);
        that.fetching_more_fotos = false;
        that.fotos_offset += data.children.length;
        if (that.fotos_request_count != data.children.length)
          that.fetched_all_fotos = true;
        $.each(data.children, function(i, c) {
          var thumb = $('<li><img src="'+c.thumbnail+'"/><br/></li>');
          $('<span></span>').text(c.title).appendTo(thumb);
          if (c.type == 'album') {
            thumb.click(function(){
              that.change_path(c.path);
            });
          }
          thumb.appendTo('#fotos');
        });
        setTimeout(function(){that.on_scroll()});
      });
  };

  KNF.prototype.on_scroll = function() {
    if (this.fetching_more_fotos || this.fetched_all_fotos)
      return;
    var diff = $(document).height()
                  - $(window).scrollTop()
                  - $(window).height();
    if (diff >= 200)
      return;
    this.fetch_more_fotos();
  };

  KNF.prototype.api = function(data, cb) {
    $.post(fotos_api_url, {
      csrfmiddlewaretoken: csrf_token,
      data: JSON.stringify(data),
    }, cb, "json");
  };

  KNF.prototype.run = function() {
    var that = this;
    this.change_path('');
    $(window).scroll(function(){that.on_scroll();});
  };

  $(document).ready(function(){
    knfotos = new KNF();
    knfotos.run();
  });
})();

/* vim: set et sta bs=2 sw=2 : */
