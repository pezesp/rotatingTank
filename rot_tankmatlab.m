%Rotating Tank
clear


r=linspace(0, 23, 23);
theta=linspace(0,2*pi, 120);
[R, THETA]=meshgrid(r, theta);

%Mesh in castesian system
X=R.*cos(THETA);
Y=R.*sin(THETA);
Y2=Y';
V=rdmds('V');
T=rdmds('T');
W=rdmds('W');

for m=1:29
    V2=V(:,:,m);
    T2=T(:,:,m);
    W2=W(:,:,m);
    
    %Plot the surface
    %Pueden ser individualmente (figure()) o juntas con subplot
    
    %Componente V - 
    %subplot(3,1,1)
%     figure(1)
%     contourf(X,Y,V2);
%     colorbar
%     xlabel('x')
%     ylabel('y')
%     title(['Componente V, layer z=', num2str(m)])
%     pause (0.5)
    
    %subplot(3,1,2)
%     figure(2)
%     contourf(X,Y,W2);
%     colorbar
%     xlabel('x')
%     ylabel('y')
%     title(['Componente W, layer z=', num2str(m)])
%     pause (0.5)
%     
%     %subplot(3,1,3)
    figure(3)
    contourf(X,Y,T2);
    colorbar
    xlabel('x')
    ylabel('y')
    title(['T, layer z=', num2str(m)])
    pause (0.5)
%     
    
end
    
   