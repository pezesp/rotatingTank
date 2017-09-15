V=rdmds('V')
for m=1:23
    Vm = V(:,:,m)
    filename = sprintf('V%02d.dat', m)
    %filename = ['V', int2str(m), '.dat'];
    save(filename, 'Vm', '-ascii');
end
