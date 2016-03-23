import jquery from 'jquery';
import Planting from 'plantingjs';
import { View } from 'backbone';


export default View.extend({

  initialize: function(options) {
    this.$el = jquery('.viewport');
    this.manifestoUrl = options.manifestoUrl;
    this.googleApiKey = options.googleApiKey;
    this.saveUrl = options.saveUrl;
    this.render();
  },

  render: function() {
    return new Planting( {
      container: this.$el,
      manifestoUrl: this.manifestoUrl,
      googleApiKey: this.googleApiKey,
      saveUrl: this.saveUrl,
      selectPanoMode: true,
      onSelectPano: this.on_select_piano.bind(this),
    });
  },

  on_select_piano: function(campaign) {
    jquery.ajax({
      type: 'POST',
      url: this.saveUrl,
      data: JSON.stringify(campaign),
      contentType: 'application/json;charset=UTF-8',
      dataType: 'html',
      success: function(responseData) {
        jquery(location).attr('href', JSON.parse(responseData).url);
      },
    });
  },

});
