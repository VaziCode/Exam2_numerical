def NevilleInterpolation(x, x_list, y_list,m,n):

    if(n-m == 1):
        result = (((x-x_list[m])*y_list[n])-((x-x_list[n])
            *y_list[m]))/(x_list[n]-x_list[m])
        print(m,'|',n,'|',"%.7f"%(result))
        return result
    result =(((x-x_list[m])*NevilleInterpolation(x,x_list,y_list,m+1,n))-((x-x_list[n])
            *NevilleInterpolation(x,x_list,y_list,m,n-1)))/(x_list[n]-x_list[m])
    print(m,'|',n,'|',"%.7f"%(result))
    return result

x_list=[0.2,0.35,0.45,0.6,0.75,0.85,0.9]
y_list=[13.7241,13.9776,14.0625,13.9776,13.7241,13.3056,12.7281]
print(NevilleInterpolation(0.65,x_list,y_list,0,len(x_list)-1))

