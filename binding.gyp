{
  'targets': [
    {
      'target_name': 'pHash',
      'sources': [ 'phash.cpp' ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'include_dirs':['/app/.apt/usr/include'],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ],
      'link_settings': {
        'libraries': ['-L/app/.apt/usr/lib']
      }
    }
  ]
}

