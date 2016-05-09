Relevant info
=============

About me
---------
in first place, because we're talking about relevant info.

Trace
-----
<https://docs.python.org/3.5/library/sys.html#sys.settrace>
<https://docs.python.org/3.5/library/inspect.html#types-and-members>

Profile
-------
<https://docs.python.org/3.5/library/profile.html>

wsgi
----
spec: <https://docs.python.org/3.5/library/wsgiref.html>

django adapter:

.. code:: python

  import os
  import os.path
  import cProfile as profile
  from django.core.wsgi import get_wsgi_application

  django_application = get_wsgi_application()

  def application(environ, start_response):
      """ wsgi application middleware """
      response_body = []
      def catching_start_response(status, headers, exc_info=None):
          """ wsgi start_response wrapper for streaming responses """
          start_response(status, headers, exc_info)
          return response_body.append

      def wrapper():
          """ wrapper for streaming wsgi responses """
          response = django_application(environ, catching_start_response)
          response_body.extend(response)
          if hasattr(response, 'close'):
              response.close()

      # profiling
      p = profile.Profile()
      p.runcall(wrapper)
      response = b''.join(response_body)

      # create profile file in tmp with url-based filename
      filename = '/tmp/{}.{}'.format(
          environ['REQUEST_METHOD'],
          environ.get('PATH_INFO').strip('/').replace('/', '.') or 'root'
          )
      p.dump_stats(filename)
      return [response]


profile
-------
python -m profile -o script.profile script.py

python -m cProfile -o script.profile script.py

profile visualizers
-------------------
runsnake script.profile (only python2)
snakeviz script.profile (only cprofile files)
