close all;
clear all;
clc;

fprintf('Starting ...\n');

D = 1;

host = '127.0.0.1';
port = 1717;
sleeping_time = 0.0001;

t = tcpip(host, port, 'NetworkRole', 'client', 'InputBufferSize', 1048576);
try
    fprintf('Starting TCP Connection to %s:%d ...\n', host, port);
    fopen(t);
    fprintf('TCP Connection to %s:%d successfully established!\n', host, port);    
    
    pause(sleeping_time);
    
    % Global Header - Only Once for Connection!!!!
    globalHeader = fread(t, 24);
    version = uint8(globalHeader(1));
    header_size = uint8(globalHeader(2));    
    pid = typecast(uint8(globalHeader(3:6)), 'uint32');
    real_width = typecast(uint8(globalHeader(7:10)), 'uint32');
    real_height = typecast(uint8(globalHeader(11:14)), 'uint32');
    virtual_width = typecast(uint8(globalHeader(15:18)), 'uint32');
    virtual_height = typecast(uint8(globalHeader(19:22)), 'uint32');
    display_orientation = uint8(globalHeader(23));
    quirk_flag = uint8(globalHeader(24));
    
    pause(sleeping_time);
    
    i = 0;
    while i < D
        % Real Reading - 2 Reads: 1st for Packet size and 2nd for data!
        packet_size_raw = fread(t, 4);
        packet_size = typecast(uint8(packet_size_raw), 'uint32');
        packet_size = double(packet_size);
        
        data_raw = fread(t, packet_size);
        
        % When Screen is Portait
        % w = virtual_width;
        % h = virtual_height;
        
        % When Screen is Landscape
        % w = virtual_height;
        % h = virtual_width;
        
        i = i + 1;
        
        pause(sleeping_time);
    end
    
    
catch me
    fprintf('Error during TCP/IP reading: %s\n', me.message);	
end

fclose(t);
fprintf('TCP socket on %s:%d closed!\n', host, port);
delete(t);
fprintf('TCP socket on %s:%d destroyed!\n', host, port);

fprintf('Completed\n');
