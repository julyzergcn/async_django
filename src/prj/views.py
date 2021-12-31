import asyncio, time
import httpx

from django.http import JsonResponse, HttpResponse


def index(request):
    return JsonResponse({'ret': 'hello'})


async def http_call_async():
  for num in range(1,6):
    await asyncio.sleep(1)
    print(num)
  async with httpx.AsyncClient() as client:
    r = await client.get("http://localhost:8000")
    print(r)


async def async_view(request):
  loop = asyncio.get_event_loop()
  loop.create_task(http_call_async())
  return HttpResponse('Non-blocking HTTP request')


def http_call_sync():
    for num in range(1, 6):
        time.sleep(1)
        print(num)
    r = httpx.get("http://localhost:8000")
    print(r)


def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")
