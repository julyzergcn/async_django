import asyncio, time, random
import httpx

from django.http import JsonResponse


def index(request):
    return JsonResponse({'ret': 'index'})


async def http_call_async():
    for num in range(random.randint(1, 3)):
        await asyncio.sleep(1)
        print(num + 1)
    async with httpx.AsyncClient() as client:
        r = await client.get("http://localhost:8000")
        print(r)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return JsonResponse({'ret': 'Async view'})


def sync_view(request):
    # sync call
    for num in range(random.randint(1, 3)):
        time.sleep(1)
        print(num + 1)
    r = httpx.get("http://localhost:8000")
    print(r)
    return JsonResponse({'ret': 'Sync view'})


async def concurrent_call(request):
    context = {}
    try:
        async with httpx.AsyncClient() as client:
            res_async, res_sync = await asyncio.gather(
                client.get('http://localhost:8000/async-view/'),
                client.get('http://localhost:8000/sync-view/'),
            )
            if res_async.status_code == httpx.codes.OK:
                context['async_view'] = res_async.json()
            if res_sync.status_code == httpx.codes.OK:
                context['sync_view'] = res_sync.json()
    except httpx.RequestError as exc:
        print(f'Error requesting {exc.request.url!r}')
    return JsonResponse(context)
