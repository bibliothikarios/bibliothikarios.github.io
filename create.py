import urllib.parse
import json

IPFS_BASE = "https://ipfs.io/ipfs/{}?filename={}"

resources = json.load(open('resources.json'))

content = ''
for idx, (dirname, displayname, dirid) in enumerate(sorted(resources['dirnames'], key=lambda x: x[1])):
    lst = '\n'.join([
        '''
        <li>
          <a href="{}" target="_blank">
            {}
          </a>
        </li>
        '''.format(
            IPFS_BASE.format(cid, urllib.parse.quote(fname)),
            fname
        ) for (cid, fname) in sorted(resources[dirname], key=lambda x: x[1])
    ])

    content += '''
      <div class="tab">'
        <input type="checkbox" id="chck{}">
        <label class="tab-label" for="chck{}">{}</label>
        <div class="tab-content">
          <p>
            <ul>
              {}
            </ul>
          </p>
        </div>
      </div>
    '''.format(idx, idx, displayname, lst)

html = open('./assets/template.html').read()
html = html.replace('{{css}}', open('./assets/style.css').read())
html = html.replace('{{content}}', content)

open('index.html', 'w').write(html)
