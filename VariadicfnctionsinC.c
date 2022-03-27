int sum(int count, ...)
{
    va_list arr;
    int t = 0;
    va_start(arr, count);
    while(count--){
        t += va_arg(arr, int);
    }
    return t;
}

int min(int count, ...)
{
    va_list arr;
    int mn = MIN_ELEMENT;
    va_start(arr, count);
    while(count--){
        if(mn > va_arg(arr, int))
            mn = va_arg(arr, int);
    }
    return mn;
}

int max(int count, ...)
{
    va_list arr;
    int mx = MAX_ELEMENT;
    va_start(arr, count);
    while(count--){
        if(mx < va_arg(arr, int))
            mx = va_arg(arr, int);
    }
    return mx;
}


