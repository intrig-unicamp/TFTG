killall bf_switchd
killall run_switchd



bf_kdrv_mod_load $SDE_INSTALL

/$SDE/../tools/p4_build.sh files/tftg.p4



/$SDE/run_switchd.sh -p tftg &

sleep 30


#Config PORTS
/$SDE/run_bfshell.sh -f files/portConfig.txt 

#Config Tables, Registers etc
/$SDE/run_bfshell.sh -b files/tftgControlPlane.py 

sleep 10

#Install rules for traffic generation
nohup python3 files/TGEntries.py > log &

#rate-show
/$SDE/run_bfshell.sh -f files/view



killall bf_switchd
