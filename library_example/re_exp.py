import re
import string

g = re.search('.', 'abcdef') # '.' (Dot.) In the default mode, this matches any character except a newline. Result 'a'
g = re.search('.', '\n')     # newline symbol, '.' (Dot.) can not match
g = re.search('.', '\n', flags=re.DOTALL)  # with flag DOTALL, '.' (Dot.) can match newline symbol

g = re.search('^B', 'A: line1\nB: line2\nC: line3')         # no match
g = re.search('^B', 'A: line1\nB: line2\nC: line3', flags=re.MULTILINE) # match line 2 start 'B'
g.group(0)  
 
g = re.search('2$', 'A: line1\nB: line2\nC: line3')         # no match
g = re.search('2$', 'A: line1\nB: line2\nC: line3', flags=re.MULTILINE) # match line 2 end with '2'
g.group(0)

rule = re.compile('a*')         # repetition of a, 'a', 'aa', 'aaa', 'aa...' matches
g = rule.match('abb a ab')
g.group(0)  # a

rule = re.compile('ab*')         # repetition of b, 'a', ab', 'abb', 'abbb', 'abbb...' matches
g = rule.match('abc a ab')
g.group(0)  # ab

rule = re.compile('ab*')         # repetition of a, 'a', 'aa', 'aaa', 'aa...' matches
g = rule.match('cdeab')
#g.group(0)  # no match None

rule = re.compile('ab*')         # * means repetion 0 or more of 'b' so match 'a'
g = rule.match('abc a ab')
g.group(0)   # a

rule = re.compile('ab+')
g = rule.match('abc a ab')       # * means repetion 1 or more of 'b' so match 'ab'
g.group(0)   # ab

rule = re.compile('ab?')
g = rule.match('c abc ab')       # Search the string from the start
g                                # None
g = rule.search('c a ab')        # Search the whole string
g.group(0)                       # 'a' , the ab? match 'a', 'ab' ? 0 or 1
g = rule.search('abc a ab')
g.group(0)                       # 'ab' substring of 'abc'

rule = re.compile('<.*>')
g = rule.search('<a> b <c>')
g.group(0)                     # '<a> b <c>'  greedy
rule = re.compile('<.*?>')
g = rule.search('<a> b <c>')
g.group(0)                     # '<a>'    non-greedy

rule = re.compile('a{6}')
g = rule.search('aaa aaaa aaaaa aaaaaa') # 'aaaaaa'
rule = re.compile('a{4,6}')
g = rule.search('aaa aaaa aaaaa aaaaaa') # 'aaaa'
rule = re.compile('a{4,6}')
g = rule.search('aaaaaaaa bbb cc d') # match the first 'aaaaaaaa' but just fetch the first 6 chars 'aaaaaa'
rule = re.compile('a{4,6}?')
g = rule.search('aaaaaaaa a aa aaa') # match the first 'aaaaaaaa' but just fetch the first 4 chars 'aaaaaa'

rule = re.compile('\*{4,6}?')
g = rule.search('******')  # '\' to escape special characters * ? 

rule = re.compile('[amk]')
g = rule.search('zdfpwfewmdsfew') # 'm'

compile_str = "-I/home/identify/github_ap_dev_11ax/wing/src/dataplane/inc -I/home/identify/github_ap_dev_11ax/wing/src/inc -I/home/identify/github_ap_dev_11ax/wing/../ADVAP/chantry/libm3msg/include -DWIOS_FEATURE_osnmp -DWIOS_FEATURE_dhcpsvr -DWIOS_FEATURE_sshd -DWIOS_FEATURE_telnetd -DWIOS_FEATURE_ftpd -DWIOS_FEATURE_pciutils -DWIOS_FEATURE_dataplane -DWIOS_FEATURE_kernel_dataplane -DWIOS_FEATURE_fw_dataplane -DWIOS_FEATURE_mint -DWIOS_FEATURE_l3fw_dataplane -DWIOS_FEATURE_fw_syn_cookies_dataplane -DWIOS_FEATURE_nat_dataplane -DWIOS_FEATURE_l2_nat_dataplane -DWIOS_FEATURE_crm -DWIOS_FEATURE_remove_appgw_rule -DWIOS_FEATURE_igmp_snoop_dataplane -DWIOS_FEATURE_l3e_migration -DWIOS_FEATURE_role -DWIOS_FEATURE_APN -DWIOS_FEATURE_facetime -DWIOS_FEATURE_unittest_dataplane -DWIOS_FEATURE_radiusd -DWIOS_FEATURE_radius3 -DWIOS_FEATURE_ldaps -DWIOS_FEATURE_static_link_aggregation -DWIOS_FEATURE_gui -DWIOS_FEATURE_mapi -DWIOS_FEATURE_hotspot -DWIOS_FEATURE_tacacs -DWIOS_FEATURE_symbol_krb5 -DWIOS_FEATURE_hotspot_2_0_r2 -DWIOS_FEATURE_cb_trustpoint -DWIOS_FEATURE_trouble_client -DWIOS_FEATURE_trouble_client_in_cfgd -DWIOS_FEATURE_dns_rtt -DWIOS_FEATURE_crm_enhancements -DWIOS_FEATURE_crm_using_flows -DWIOS_FEATURE_std_fdb_mibs -DWIOS_FEATURE_loop_debug -DWIOS_FEATURE_fabric_attach -DWIOS_FEATURE_l3e_diag -DWIOS_FEATURE_busybox_dhcp_client -DWIOS_FEATURE_cmcc -DWIOS_FEATURE_rate_limit -DWIOS_FEATURE_cmcc_hotspot -DWIOS_FEATURE_mu_balance -DWIOS_FEATURE_cmcc_traps -DWIOS_FEATURE_smart -DWIOS_FEATURE_vrrp -DWIOS_FEATURE_dynamic_routing -DWIOS_FEATURE_fib -DWIOS_FEATURE_ext_vlan_load_balancing -DWIOS_FEATURE_ssm -DWIOS_FEATURE_l2tpv3 -DWIOS_FEATURE_pptp_alg -DWIOS_FEATURE_l2tpv3_rate_limit -DWIOS_FEATURE_ext_vlan_ovr_mint_level2_rate_limit -DWIOS_FEATURE_certmgr_dpd2 -DWIOS_FEATURE_ldap_rbfw -DWIOS_FEATURE_multibyte_ssid -DWIOS_FEATURE_mschapv2_ldap -DWIOS_FEATURE_cmp -DWIOS_FEATURE_bonjour_gateway -DWIOS_FEATURE_xcbc_crypto -DWIOS_FEATURE_ipsec_dataplane -DWIOS_FEATURE_vpn2 -DWIOS_FEATURE_swcrypto -DWIOS_FEATURE_ipv6 -DWIOS_FEATURE_fib6 -DWIOS_FEATURE_snmp_acl -DWIOS_FEATURE_dhcp_fingerprinting -DWIOS_FEATURE_dns_in_acl -DWIOS_FEATURE_dhcp_alps -DWIOS_FEATURE_mart_client -DWIOS_FEATURE_alarm -DWIOS_FEATURE_gm_client -DWIOS_FEATURE_zguest_ui -DWIOS_FEATURE_cvg_hole_incident_stats -DWIOS_FEATURE_kernel64_user32 -DWIOS_FEATURE_energy_efficient_ethernet -DWIOS_FEATURE_config_eee -DWIOS_FEATURE_chantry -DWIOS_FEATURE_multi_personality -DWIOS_FEATURE_jffs2 -DWIOS_FEATURE_virtual_mgmt_port -DWIOS_FEATURE_corecrypto_dataplane -DWIOS_FEATURE_dataplane_jobs -DWIOS_FEATURE_dns_svr_fwd -DWIOS_FEATURE_radio -DWIOS_FEATURE_11ac_bcm_ko -DWIOS_FEATURE_11ax_bcm_ko -DWIOS_FEATURE_gt_2_streams -DWIOS_FEATURE_bcm6x -DWIOS_FEATURE_bcm6x_no_patch -DWIOS_FEATURE_11ac_wave2 -DWIOS_FEATURE_gt_3_streams -DWIOS_FEATURE_prop_11ac_rates -DWIOS_FEATURE_11ax_rates -DWIOS_FEATURE_160_MHZ -DWIOS_FEATURE_extr_compliance -DWIOS_FEATURE_mc2uc -DWIOS_FEATURE_dot1x_pae -DWIOS_FEATURE_dot1x_auth -DWIOS_FEATURE_controller_ap -DWIOS_FEATURE_auto_vc -DWIOS_FEATURE_http_alg -DWIOS_FEATURE_http_analytics -DWIOS_FEATURE_pbr -DWIOS_FEATURE_mstp -DWIOS_FEATURE_ble_beacon -DWIOS_FEATURE_iot -DWIOS_FEATURE_power_mgmt -DWIOS_FEATURE_hotspot -DWIOS_FEATURE_compliance_d -DWIOS_FEATURE_collector -DWIOS_FEATURE_cloud_ap -DWIOS_FEATURE_cloud_adoption_config -DWIOS_FEATURE_dual_5ghz -DWIOS_FEATURE_select_shutdown -DWIOS_FEATURE_sae -DWIOS_FEATURE_wips_sensor -DWIOS_FEATURE_wips_radiotap -DWIOS_FEATURE_wips_ofl_sensor -DWIOS_FEATURE_mpact_client -DWIOS_FEATURE_rssi_feed -DWIOS_FEATURE_lsense_client -DWIOS_FEATURE_adv_spectrum_analyser -DWIOS_FEATURE_11ac_sensor -DWIOS_FEATURE_content_filtering -DWIOS_FEATURE_wing_express -DWIOS_FEATURE_application_assurance -DWIOS_FEATURE_dpi_purview -DWIOS_FEATURE_dpi_metadata -DWIOS_FEATURE_dpi_timed_rules -DWIOS_FEATURE_time_based_access -DWIOS_FEATURE_l2tpv3_fast_failover -DWIOS_FEATURE_phpcgi -DWIOS_FEATURE_broadcom_uboot -DWIOS_FEATURE_initramfs -DWIOS_FEATURE_lacp -DWIOS_FEATURE_solum_esl -DWIOS_FEATURE_koda_d -DWIOS_FEATURE_mtd -DMOTO_TARGET_sequoia -DTARGET_sequoia -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/router/hnd_wl/wl_apsta_eap//../../../../../main/src/wl -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/router/hnd_wl/wl_apsta_eap//../../../../../main/src/wl -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/accel/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/avs/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/awd/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/bcmcrypto/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/clm-api/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/math/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/msch/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/old -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/hal -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/ac/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/n/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/lcn20/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/utils -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/wd -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/init -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/ana -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/antdiv -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/btcx -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/cache -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/calmgr -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/chanmgr -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/core -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/dccal -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/dbg -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/dsi -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/et -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/fcbs -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/hirssi -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/lpc -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/misc -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/mu -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/nap -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/noise -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/papdcal -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/radar -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/radio -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/rssi -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/rxgcrs -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/rxiqcal -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/rxspur -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/samp -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/tbl -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/temp -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/tof -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/tpc -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/txpwrcap -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/tssical -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/txiqlocal -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/vcocal -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/ocl -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/hecap -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/prephy -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/hc -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/vasip -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/stf -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/cmn/smc -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/ac/core -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/n/core -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/lcn20/core -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/ac/dsi -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/ac/papdcal -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/ac/et -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/ac/samp -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/phy/ac/radio -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/proto/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/wlioctl/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/shared/bcmwifi/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/chctx/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/dump/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/encode/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/gas/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/iocv/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/keymgmt/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/mbo_oce/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/olpc/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/ppr/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/shared -DWL_ALL_PASSIVE -DDMA -DWLTEST -DWL_EXPORT_CURPOWER -DBCMDBG -DRSDB_PARALLEL_SCAN_DISABLED -DPPR_API -DWLATF -DWL_AP_CHAN_CHANGE_EVENT -DBCM_CEVENT -DSPLIT_ASSOC -DBCM_DMA_CT -DBCM_DMA_INDIRECT -DWLATF_PERC -DWLWRR -DCHAN_SWITCH_HIST -DPSPRETEND -DWL_CS_PKTRETRY -DWL_CS_RESTRICT_RELEASE -DBCMDBG_TRAP -DWL_PROT_OBSS -DWL_OBSS_DYNBW -DWLWSEC -DWL11N -DWL11AC -DWL11AC_160 -DWL_BEAMFORMING -DTXBF_MORE_LINKS -DWLOLPC -DWL11AX -DWLPKTENG -DWLTWT -DTESTBED_AP_11AX -DWL_MODESW -DPHYCAL_CACHING -DWL_MU_TX -DWL_MU_RX -DWL_MUSCHEDULER -DWL_PSMX -DWL_PSMR1 -DWL_AUXPMQ -DWL11H -DWLCSA -DWLQUIET -DWLTPC -DWL_AP_TPC -DWL_CHANSPEC_TXPWR_MAX -DBGDFS -DBGDFS_2G -DWL_DFS_TEST_MODE -DWL_SCAN_DFS_HOME -DWL11D -DWLCNTRY -DWL_BSS_INFO_TYPEDEF_HAS_ALIAS -DRATESET_VERSION_ENABLED -DWL_CFG80211 -DUSE_CFG80211 -DWL_CFG80211_NIC -DSUPPORT_SOFTAP_WPAWPA2_MIXED -DWL_VENDOR_EXT_SUPPORT -DROUTER_CFG -DWL_SAE -DWL_STAPRIO -DAP -DMULTIAP -DWL_GLOBAL_RCLASS -DMBSS -DWL_EAP_MBSS_BCNROTATE -DWDS -DDWDS -DAPCS -DWME_PER_AC_TX_PARAMS -DWME_PER_AC_TUNING -DSTA -DWET -DRXCHAIN_PWRSAVE -DRADIO_PWRSAVE -DWL_IGMP_UCQUERY -DWL_UCAST_UPNP -DMCAST_REGEN -DWLOVERTHRUSTER -DMAC_SPOOF -DIBSS_PEER_GROUP_KEY -DIBSS_PSK -DIBSS_PEER_MGMT -DIBSS_PEER_DISCOVERY_EVENT -DWLLED -DWL_MONITOR -DWL_NEW_RXSTS -DWL_RADIOTAP -DWL_STA_MONITOR -DWME -DWL11H -DWL11D -DWL11U -DWLPROBRESP_SW -DWLPROBRESP_MAC_FILTER -DDBAND -DWLRM -DWLCQ -DWLCNT -DWLTAF -DDELTASTATS -DWLCHANIM -DWLCNTSCB -DWLSCB_HISTO -DWLCOEX -DWLOSEN -DWLFBT -DBCMINTSUP -DWLCHANIM_US -DBCMSUP_PSK -DBCMINTSUP -DWLCAC -DMFP -DBCMCCMP -DWLAMSDU -DWLAMSDU_SWDEAGG -DWLNAR -DWLAMPDU -DWLAMPDU_MAC -DWLDLS -DWLBSSLOAD -DL2_FILTER -DWIFI_ACT_FRAME -DWL_IOVF_RSDB_SET -DWLPKTDLYSTAT -DWLPKTDLYSTAT_IND -DHNDBME -DBCMNVRAMR -DBCMNVRAMW -DBCMNVRAMR -DWLTINYDUMP -DWL11K_AP -DWL11K -DWL11K_ALL_MEAS -DWL11K_BCN_MEAS -DWL11K_NBR_MEAS -DWLWNM_AP -DWLWNM -DWL_MBO -DMBO_AP -DWL_EVENTQ -DWL_GLOBAL_RCLASS -DSAMPLE_COLLECT -DSMF_STATS -DPHYMON -DBCM_DCS -DPHY_HAL -DWET_TUNNEL -DWLHEB -DWL_EAP_AP -DWL_EAP_PER_VAP_CONFIG -DWL_EAP_PER_VAP_DTIM -DWL_EAP_PER_VAP_AMSDU_HWDAGG_DIS -DWL_EAP_SAMPLE_COLLECT -DWL_EAP_PRS_RTX_LIMIT -DWL_EAP_STATS -DBCMDBG_AMPDU -DWL_EAP_SNR -DWL_EAP_FFT_SAMPLE -DWL_EAP_ACK_RSSI -DAVS -DAVS_ENABLE_LVM -DAVS_GET_BOARD_DAC_CODE -DAVS_FIND_NOMINAL_VOLTAGE -DAVS_ENABLE_STATUS -DBULKRX_PKTLIST -DSTS_FIFO_RXEN -DBME_OFFLOADS_RXSTS -DWL_MCAST_FILTER_NOSTA -DBCMCRYPTO_COMPONENT -DWL_RATELINKMEM -DWL_EAP_SCAN_TX -DWL_EAP_STA_SCB_TIMEOUT -DWL_EAP_PER_VAP_CONFIG -DWL_EAP_UCODE -DWL_EAP_PER_VAP_PKTC -DWL_EAP_EMSGLVL -DWL_EAP_TPDUMP -DWL_EAP_LAST_PKT_RSSI -DWL_EAP_EVENT_SERVICE -DWL_EAP_CUSTOM_SCAN -DWL_EAP_SCAN_MEASUREMENT -DWL_EAP_SCAN_TEST -DWL_EAP_SCAN_PROTECT -DWL_EAP_SCAN_BEACON_DELAY -DWL_EAP_DATA_SNOOP -D WL_EAP_RUNT_ON_BADFCS_FRM -DWL_EAP_NOISE_MEASUREMENTS -DWL_EAP_OLPC -DWL_EAP_MONITOR -DWL_EAP_ALLOW_MESH_FRM -DWL_EAP_ALLOW_MGMT_FRM -DWL_EAP_ALLOW_SOUND_FB -DWL_EAP_PER_VAP_CONFIG_RATESET -DWL_EAP_DROP_RX_MGMT_RSSI -DWL_EAP_BOARD_RF_5G_FILTER -DWL_EAP_KEY_CACHE -DWL_EAP_CUST_EVENT_HNDLR -DWL_EAP_OUTDOOR_AP -DFRAMEBURST_RTSCTS_PER_AMPDU -DTUNE_FBOVERRIDE -DWL_TRAFFIC_THRESH -DWL_EAP_DFS_ALTMODE -DBCM_SKB_FREE_OFFLOAD -DWL_EAP_PKTCNTR -Werror -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/router/hnd_wl/wl_apsta_eap/ -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/router/hnd_wl/wl_apsta_eap//.. -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/linux -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/sys -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/dot1as/include -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/dot1as/src -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/wl/proxd/include -Idrivers/bcmdrivers/opensource/include/bcm963xx -Idrivers/bcmdrivers/broadcom/include/bcm963xx -Idrivers/bcmdrivers/shared/opensource/include/bcm963xx -finline-limit=2048 -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/router/hnd_wl/wl_apsta_eap//../../../../../main/src/../components/router/dpsta -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/components/router/hnd_wl/wl_apsta_eap//../../../../../main/src/../components/phy/old -DBCMDBG_PHYDUMP -std=gnu99 -Wno-declaration-after-statement -I/home/identify/github_ap_dev_11ax/wing/obj/sequoia/src/radio/bcm/bcm_driver/wl/impl51/main/src/../../../shared/impl1 -DBCM_BLOG -DBCM_NBUFF -DBCM_NBUFF_PKT -Idrivers/bcmdrivers/shared/opensource/include/bcm963xx -DBULK_PKTLIST -DSTS_FIFO_RXEN"
option_list = re.findall(r'-D\w+',compile_str)
for str in option_list:
    print(str)

rule = re.compile('\s')
g = rule.search(' ')
g = rule.search('\t')
g = rule.search('\n')
g = rule.search('\r')
print(g.group(0))     # match one space and Matches Unicode whitespace characters (which includes [ \t\n\r\f\v])
rule = re.compile('\S')
g = rule.search('\n')
#print(g.group(0))     # \S doesn't match white space character which excludes [ \t\n\r\f\v]

rule = re.compile('\w')
g = rule.search('王')
print(g.group(0))     # match any Unicode character even Chinese word character
rule = re.compile('\W')
g = rule.search('王')
#print(g.group(0))     # doesn't match word character

rule = re.compile('\d')
g = rule.search('1')
print(g.group(0))     # match any decimal digit [0-9]
rule = re.compile('\D')
g = rule.search('1')
#print(g.group(0))     # doesn't match a decimal digit [^0-9]

re.split(r'\W+', 'Words, words, words.')
# ['Words', 'words', 'words', '']
re.split(r'(\W+)', 'Words, words, words.')
# ['Words', ', ', 'words', ', ', 'words', '.', '']
re.split(r'\W+', 'Words, words, words.', 1)
# ['Words', 'words, words.']
re.split('[abf]+', '0a3B9F7', flags=re.IGNORECASE)
# ['0', '3', '9', '7']
re.split(r'(\W+)', '...words, words...')r
# ['', '...', 'words', ', ', 'words', '...', '']

it1 = re.finditer(r'\w+', 'Words, words, words.')
for i in it1:
    print(i.group())  # Words, words, words
l1 = re.findall(r'\w+', 'Words, words, words.')
for i in l1:
    print(i)          # Words, words, words
it1 = re.finditer(r'\W+', 'Words, words, words.')
for i in it1:
    print(i.group())  # , , .
l1 = re.findall(r'\W+', 'Words, words, words.')
for i in l1:
    print(i)          # , , .
it1 = re.finditer(r'[Ww][oO][Rr][dD]', 'Words, words, words.')
for i in it1:
    print(i.group())  # Word word word

inputStr = "hello 123 world 456 bye 789"
replacedStr = re.sub(r'\d+', '111', inputStr, 2)
print(replacedStr)   # hello 111 world 111 bye 789

inputStr = "hello 123 world 456 bye 789" 
replacedStr = re.subn(r'\d+', '111', inputStr, 2)   # return a tuple with replace count
print(replacedStr)

def PythonReSub():
    inputStr = "hello 123 world 456 bye 789"
    
    def _add111(matched):
        input_num_str = matched.group("number")
        input_num_value = int(input_num_str)
        output_num_value = input_num_value + 111
        output_num_str = str(output_num_value)
        return output_num_str
    
    replacedStr = re.sub("(?P<number>\d+)", _add111, inputStr)
    print("replacedStr=",replacedStr)
if __name__=="__main__":
    PythonReSub();

print(re.escape('python.exe'))
legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`"
print('[%s]+' % re.escape(legal_chars))

text = """Ross McFluff: 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""
entries = re.split(r'\n', text)
print(entries)
['Ross McFluff: 834.345.1254 155 Elm Street',
 '',
 'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
 'Frank Burger: 925.541.7625 662 South Dogwood Way',
 '',
 '',
 'Heather Albrecht: 548.326.4584 919 Park Place']

entries = re.split(r'\n+', text)
print(entries)
['Ross McFluff: 834.345.1254 155 Elm Street',
 'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
 'Frank Burger: 925.541.7625 662 South Dogwood Way',
 'Heather Albrecht: 548.326.4584 919 Park Places']

 text = """Ross McFluff, 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""
entries = re.split(r'\n+', text)
print(entries)
['Ross McFluff: 834.345.1254 155 Elm Street',
 'Ronald Heathmore: 892.345.3428 436 Finley Avenue',
 'Frank Burger: 925.541.7625 662 South Dogwood Way',
 'Heather Albrecht: 548.326.4584 919 Park Places']
[re.split("[:,]? ", entry, 3) for entry in entries]
[['Ross', 'McFluff,', '834.345.1254', '155 Elm Street'],
 ['Ronald', 'Heathmore', '892.345.3428', '436 Finley Avenue'],
 ['Frank', 'Burger', '925.541.7625', '662 South Dogwood Way'],
 ['Heather', 'Albrecht', '548.326.4584', '919 Park Place']]
[re.split("[:,]? ", entry, 4) for entry in entries]
[['Ross', 'McFluff', '834.345.1254', '155', 'Elm Street'],
 ['Ronald', 'Heathmore', '892.345.3428', '436', 'Finley Avenue'],
 ['Frank', 'Burger', '925.541.7625', '662', 'South Dogwood Way'],
 ['Heather', 'Albrecht', '548.326.4584', '919', 'Park Place']]