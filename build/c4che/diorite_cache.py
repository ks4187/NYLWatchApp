AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'diorite'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'diorite'
BUNDLE_NAME = 'NYLWatchApp.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_DIORITE', 'PBL_BW', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_HEALTH', 'PBL_SMARTSTRAP', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'darwin'
INCLUDES = ['diorite']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = []
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'WEATHER_ICON_KEY': 0, u'WEATHER_TEMPERATURE_KEY': 1, u'WEATHER_CITY_KEY': 2}
MESSAGE_KEYS_DEFINITION = '/Users/karanshah/Documents/projects/NYLWatchApp/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/Users/karanshah/Documents/projects/NYLWatchApp/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/Users/karanshah/Documents/projects/NYLWatchApp/build/js/message_keys.json'
NODE_PATH = '/Users/karanshah/Library/Application Support/Pebble SDK/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/Users/karanshah/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/Users/karanshah/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/diorite'
PEBBLE_SDK_ROOT = '/Users/karanshah/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['diorite', 'bw', 'rect', 'mic', 'strap', 'health', '144w', '168h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'diorite', 'BUNDLE_BIN_DIR': 'diorite', 'BUILD_DIR': 'diorite', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_DIORITE', 'PBL_BW', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_HEALTH', 'PBL_SMARTSTRAP', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168']}
PLATFORM_NAME = 'diorite'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {u'WEATHER_ICON_KEY': 0, u'WEATHER_TEMPERATURE_KEY': 1, u'WEATHER_CITY_KEY': 2}, u'sdkVersion': u'3', u'projectType': u'native', u'uuid': u'74460383-8a0f-4bb6-971f-8937c2ed4441', u'messageKeys': {u'WEATHER_ICON_KEY': 0, u'WEATHER_TEMPERATURE_KEY': 1, u'WEATHER_CITY_KEY': 2}, 'companyName': u'Pebble Technology', u'enableMultiJS': False, u'targetPlatforms': [u'aplite', u'diorite', u'emery'], 'versionLabel': u'2.0', 'longName': u'PebbleJS Weather', u'displayName': u'PebbleJS Weather', 'shortName': u'PebbleJS Weather', u'watchapp': {u'watchface': False}, u'resources': {u'media': [{u'targetPlatforms': None, u'type': u'bitmap', u'name': u'IMAGE_LOGO', u'file': u'images/logo.png'}, {u'type': u'bitmap', u'name': u'IMAGE_SUN', u'file': u'images/sun.png'}, {u'type': u'bitmap', u'name': u'IMAGE_SNOW', u'file': u'images/snow.png'}, {u'type': u'bitmap', u'name': u'IMAGE_RAIN', u'file': u'images/rain.png'}, {u'type': u'bitmap', u'name': u'IMAGE_CLOUD', u'file': u'images/cloud.png'}]}, 'name': u'pebblejs-weather'}
REQUESTED_PLATFORMS = [u'aplite', u'diorite', u'emery']
RESOURCES_JSON = [{u'targetPlatforms': None, u'type': u'bitmap', u'name': u'IMAGE_LOGO', u'file': u'images/logo.png'}, {u'type': u'bitmap', u'name': u'IMAGE_SUN', u'file': u'images/sun.png'}, {u'type': u'bitmap', u'name': u'IMAGE_SNOW', u'file': u'images/snow.png'}, {u'type': u'bitmap', u'name': u'IMAGE_RAIN', u'file': u'images/rain.png'}, {u'type': u'bitmap', u'name': u'IMAGE_CLOUD', u'file': u'images/cloud.png'}]
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 86
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['aplite', 'basalt', 'chalk', 'diorite', 'emery']
TARGET_PLATFORMS = ['emery', 'diorite', 'aplite']
TIMESTAMP = 1507584503
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/Users/karanshah/Library/Application Support/Pebble SDK/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
