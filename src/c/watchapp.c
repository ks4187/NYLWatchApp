#include "pebble.h"

static Window *s_main_window;

static TextLayer *s_temperature_layer;
static TextLayer *s_city_layer;
static TextLayer *s_confirm_layer;
static BitmapLayer *s_icon_layer;
static BitmapLayer *s_confirm_bitmap_layer;
static GBitmap *s_icon_bitmap = NULL;
static GBitmap *s_confirmation_bitmap = NULL;

static AppSync s_sync;
static uint8_t s_sync_buffer[64];

enum WeatherKey {
  WEATHER_ICON_KEY = 0x0,         // TUPLE_INT
  WEATHER_TEMPERATURE_KEY = 0x1,  // TUPLE_CSTRING
  WEATHER_CITY_KEY = 0x2,         // TUPLE_CSTRING
};

static const uint32_t WEATHER_ICONS[] = {
  RESOURCE_ID_IMAGE_SUN, // 0
  RESOURCE_ID_IMAGE_CLOUD, // 1
  RESOURCE_ID_IMAGE_CONFIRM, // 2
  RESOURCE_ID_IMAGE_SNOW, // 3
  RESOURCE_ID_IMAGE_LOGO, // 4
  RESOURCE_ID_IMAGE_CONFIRM // 5
};

static void sync_error_callback(DictionaryResult dict_error, AppMessageResult app_message_error, void *context) {
  APP_LOG(APP_LOG_LEVEL_DEBUG, "App Message Sync Error: %d", app_message_error);
}

static void sync_tuple_changed_callback(const uint32_t key, const Tuple* new_tuple, const Tuple* old_tuple, void* context) {
  switch (key) {
    case WEATHER_ICON_KEY:
      if (s_icon_bitmap) {
        gbitmap_destroy(s_icon_bitmap);
      }

      s_icon_bitmap = gbitmap_create_with_resource(WEATHER_ICONS[new_tuple->value->uint8]);
      bitmap_layer_set_compositing_mode(s_icon_layer, GCompOpSet);
      bitmap_layer_set_bitmap(s_icon_layer, s_icon_bitmap);
      break;

    case WEATHER_TEMPERATURE_KEY:
      // App Sync keeps new_tuple in s_sync_buffer, so we may use it directly
      text_layer_set_text(s_temperature_layer, new_tuple->value->cstring);
      break;

    case WEATHER_CITY_KEY:
      text_layer_set_text(s_city_layer, new_tuple->value->cstring);
      break;
  }
}

static void request_weather(void) {
  DictionaryIterator *iter;
  app_message_outbox_begin(&iter);

  if (!iter) {
    // Error creating outbound message
    return;
  }

  int value = 1;
  dict_write_int(iter, 1, &value, sizeof(int), true);
  dict_write_end(iter);
  app_message_outbox_send();
}

static void window_load(Window *window) {
  Layer *window_layer = window_get_root_layer(window);
  GRect bounds = layer_get_bounds(window_layer);

  s_icon_layer = bitmap_layer_create(GRect(0, 10, bounds.size.w, 80));
  layer_add_child(window_layer, bitmap_layer_get_layer(s_icon_layer));

  s_confirm_bitmap_layer = bitmap_layer_create(GRect(0, 10, bounds.size.w, 80));


  s_temperature_layer = text_layer_create(GRect(0, 90, bounds.size.w, 32));
  text_layer_set_text_color(s_temperature_layer, GColorWhite);
  text_layer_set_background_color(s_temperature_layer, GColorClear);
  text_layer_set_font(s_temperature_layer, fonts_get_system_font(FONT_KEY_GOTHIC_28_BOLD));
  text_layer_set_text_alignment(s_temperature_layer, GTextAlignmentCenter);
  layer_add_child(window_layer, text_layer_get_layer(s_temperature_layer));

  s_city_layer = text_layer_create(GRect(0, 122, bounds.size.w, 32));
  text_layer_set_text_color(s_city_layer, GColorWhite);
  text_layer_set_background_color(s_city_layer, GColorClear);
  text_layer_set_font(s_city_layer, fonts_get_system_font(FONT_KEY_GOTHIC_28_BOLD));
  text_layer_set_text_alignment(s_city_layer, GTextAlignmentCenter);
  layer_add_child(window_layer, text_layer_get_layer(s_city_layer));

  s_confirm_layer = text_layer_create(GRect(0, 90, bounds.size.w, bounds.size.h));
  text_layer_set_text_color(s_confirm_layer, GColorWhite);
  text_layer_set_background_color(s_confirm_layer, GColorClear);
  text_layer_set_font(s_confirm_layer, fonts_get_system_font(FONT_KEY_GOTHIC_28_BOLD));
  text_layer_set_text_alignment(s_confirm_layer, GTextAlignmentCenter);

  Tuplet initial_values[] = {
    TupletInteger(WEATHER_ICON_KEY, (uint8_t) 4),
    TupletCString(WEATHER_TEMPERATURE_KEY, "NYL PAY"),
    TupletCString(WEATHER_CITY_KEY, "Loading..."),
  };

  app_sync_init(&s_sync, s_sync_buffer, sizeof(s_sync_buffer),
      initial_values, ARRAY_LENGTH(initial_values),
      sync_tuple_changed_callback, sync_error_callback, NULL);

  request_weather();
}

static void window_unload(Window *window) {
  if (s_icon_bitmap) {
    gbitmap_destroy(s_icon_bitmap);
  }

  text_layer_destroy(s_city_layer);
  text_layer_destroy(s_temperature_layer);
  bitmap_layer_destroy(s_icon_layer);
}

void select_single_click_handler(ClickRecognizerRef recognizer, void *context) {
  layer_remove_child_layers(window_get_root_layer(s_main_window));

  Layer *window_layer = window_get_root_layer(s_main_window);

  text_layer_set_text(s_confirm_layer, "PAYMENT CONFIRMED!");
  layer_add_child(window_layer, text_layer_get_layer(s_confirm_layer));

  s_confirmation_bitmap = gbitmap_create_with_resource((uint8_t)5);
  bitmap_layer_set_compositing_mode(s_confirm_bitmap_layer, GCompOpSet);
  bitmap_layer_set_bitmap(s_confirm_bitmap_layer, s_confirmation_bitmap);
  layer_add_child(window_layer, bitmap_layer_get_layer(s_confirm_bitmap_layer));

  //test_window_load(s_main_window);
}

void config_provider(Window *window) {
 // single click / repeat-on-hold config:
  //window_single_click_subscribe(BUTTON_ID_DOWN, down_single_click_handler);
  window_single_repeating_click_subscribe(BUTTON_ID_SELECT, 1000, select_single_click_handler);

  // multi click config:
  //window_multi_click_subscribe(BUTTON_ID_SELECT, 2, 10, 0, true, select_multi_click_handler);

  // long click config:
  //window_long_click_subscribe(BUTTON_ID_SELECT, 700, select_long_click_handler, select_long_click_release_handler);
}

static void init(void) {
  s_main_window = window_create();
  window_set_background_color(s_main_window, PBL_IF_COLOR_ELSE(GColorIndigo, GColorBlack));
  window_set_window_handlers(s_main_window, (WindowHandlers) {
    .load = window_load,
    .unload = window_unload
  });
  window_stack_push(s_main_window, true);

  window_set_click_config_provider(s_main_window, (ClickConfigProvider) config_provider);

  app_message_open(64, 64);
  
  
  //test_window_load(s_main_window);
}

static void deinit(void) {
  window_destroy(s_main_window);

  app_sync_deinit(&s_sync);
}

int main(void) {
  init();
  app_event_loop();
  deinit();
}
