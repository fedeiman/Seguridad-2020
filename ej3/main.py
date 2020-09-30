from flask import Flask, abort, redirect, request, Response
import base64, json, MySQLdb, os, re, subprocess

app = Flask(__name__)

home = '''
<!doctype html>
<html>

<head>
	<link href="https://unpkg.com/tailwindcss@^1.8.10/dist/tailwind.min.css" rel="stylesheet">
	<title>Meme's Fun Library</title>
</head>

<body>
	<div class="antialiased bg-gray-900">
		<div class="mx-auto py-12 p-16 max-w-screen-xl">
			<h1 class="text-5xl leading-9 font-extrabold text-white tracking-tight sm:text-4xl mt-2"> Meme's Fun Library
			</h1>
			$ALBUMS$
</body>

</html>
'''

viewAlbum = '''
<!doctype html>
<html>

<head>
	<title>$TITLE$ -- Meme's Fun Library</title>
</head>

<body>
	<h1>$TITLE$</h1>
	$GALLERY$
</body>

</html>
'''

def getDb():
    return MySQLdb.connect(host="localhost", user="root", password="", db="memes_db")

def sanitize(data):
    return data.replace('&', '&amp;').replace('<', '&lt;' ).replace('>', '&gt;').replace('"', '&quot;')

@app.route('/')
def index():
	cur = getDb().cursor()
	cur.execute('SELECT id, title FROM albums')
	albums = list(cur.fetchall())

	rep = ''
	for id, title in albums:
	    rep += '<h2 class="text-xl leading-7 text-indigo-400 mt-4"> %s </h2>\n' % sanitize(title)
	    rep += '<div class="bg-gray-800 my-4 py-6 flex items-center justify-evenly flex-wrap rounded">\n'
		cur.execute('SELECT id, title, filename FROM memes WHERE parent=%s LIMIT 5', (id, ))
		fns = []
		for pid, ptitle, pfn in cur.fetchall():
		    rep += '<div class="text-center">\n'
			rep += ' <img class="h-64 flex-1 rounded" src="meme?id=%i" width="266" height="150">\n' % (pid)
            rep += ' <div class="mt-2 mb-4 font-medium text-gray-200 hover:text-white text-lg leading-6">\n- %s -\n'% (sanitize(ptitle))
			rep += ' </div>\n</div>\n'
		    fns.append(pfn)
		rep += '''<div class="text-gray-300 font-semibold">
			<div class="inline-flex space-x-1 hover:text-white">
				<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
					xmlns="http://www.w3.org/2000/svg">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
						d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
				</svg>
				'''
		rep += '<i>Space used: ' + subprocess.check_output('du -ch %s || exit 0' % ' '.join('files/' + fn for fn in fns), shell=True, stderr=subprocess.STDOUT).strip().rsplit('\n', 1)[-1] + '</i>'
		rep += ' </div>\n</div>'
		rep += '</div>'
	rep += '</div>'
	return home.replace('$ALBUMS$', rep)

@app.route('/meme')
def fetch():
	cur = getDb().cursor()
	if cur.execute('SELECT filename FROM memes WHERE id=%s' % request.args['id']) == 0:
	abort(404)

	# It's dangerous to go alone, take this:
	# ^FLAG^ SEGURIDAD-OFENSIVA-FAMAF $FLAG$

	return file('./%s' % cur.fetchone()[0].replace('..', ''), 'rb').read()

	if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5010)