import jquery from 'jquery';
import Planting from 'plantingjs';
import { View } from 'backbone';


export default View.extend({

  initialize: function(options) {
    this.$el = jquery('.viewport');
    this.saveUrl = options.saveUrl;
    this.engine = new Planting( {
      container: this.$el,
      manifestoUrl: options.manifestoUrl,
      googleApiKey: options.googleApiKey,
      onSave: this.simple_save_callback.bind(this),
    });
    this.engine.initStreetview({
      lat: options.lat,
      lng: options.lng,
      heading: options.heading,
      pitch: options.pitch,
      zoom: options.zoom,
    });
  },

  simple_save_callback: function(planting) {
    jquery.ajax({
      type: 'POST',
      url: this.saveUrl,
      data: JSON.stringify(planting),
      contentType: 'application/json;charset=UTF-8',
      dataType: 'html',
      success: function(responseData) {
        jquery(location).attr('href', JSON.parse(responseData).url);
      },
    });
  },

});
