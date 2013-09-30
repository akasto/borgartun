from base import Base
class Client(Base):
    def listIsos(self, **kwargs):
        """
        account the account of the ISO file. Must be used with the domainId parameter. false
        bootable true if the ISO is bootable, false otherwise false
        domainid lists all available ISO files by ID of a domain. If used with the account parameter, lists all available ISO files for the account in the ID of a domain. false
        hypervisor the hypervisor for which to restrict the search false
        id list all isos by id false
        isofilter possible values are "featured", "self", "self-executable","executable", and "community". * featured-ISOs that are featured and are publicself-ISOs that have been registered/created by the owner. * selfexecutable-ISOs that have been registered/created by the owner that can be used to deploy a new VM. * executable-all ISOs that can be used to deploy a new VM * community-ISOs that are public. false
        ispublic true if the ISO is publicly available to all users, false otherwise. false
        isready true if this ISO is ready to be deployed false
        name list all isos by name false
        zoneid the ID of the zone false
        """
        return self.call("listIsos", args)

    def startVirtualMachine(self, **kwargs):
        """
        id The ID of the virtual machine true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("startVirtualMachine", args)

    def deleteTemplate(self, **kwargs):
        """
        id the ID of the template true
        zoneid the ID of zone of the template false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("deleteTemplate", args)

    def restartNetwork(self, **kwargs):
        """
        id The network this ip address should be associated to. true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("restartNetwork", args)

    def associateIpAddress(self, **kwargs):
        """
        zoneid the ID of the availability zone you want to acquire an public IP address from true
        account the account to associate with this IP address false
        domainid the ID of the domain to associate with this IP address false
        networkid The network this ip address should be associated to. false
        """
        if not zoneid in kwargs:
            raise RuntimeError("Missing required argument zoneid")
        return self.call("associateIpAddress", args)

    def removeFromLoadBalancerRule(self, **kwargs):
        """
        id The ID of the load balancer rule true
        virtualmachineids the list of IDs of the virtual machines that are being removed from the load balancer rule (i.e. virtualMachineIds=1,2,3) true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        if not virtualmachineids in kwargs:
            raise RuntimeError("Missing required argument virtualmachineids")
        return self.call("removeFromLoadBalancerRule", args)

    def createNetwork(self, **kwargs):
        """
        displaytext the display text of the network true
        name the name of the network true
        networkofferingid the network offering id true
        zoneid the Zone ID for the Vlan ip range true
        account account who will own the network false
        domainid domain ID of the account owning a network false
        endip the ending IP address in the VLAN IP range false
        gateway the gateway of the VLAN IP range false
        isdefault true if network is default, false otherwise false
        isshared true is network offering supports vlans false
        netmask the netmask of the VLAN IP range false
        networkdomain network domain false
        startip the beginning IP address in the VLAN IP range false
        vlan the ID or VID of the VLAN. Default is an "untagged" VLAN. false
        """
        if not displaytext in kwargs:
            raise RuntimeError("Missing required argument displaytext")
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        if not networkofferingid in kwargs:
            raise RuntimeError("Missing required argument networkofferingid")
        if not zoneid in kwargs:
            raise RuntimeError("Missing required argument zoneid")
        return self.call("createNetwork", args)

    def deletePortForwardingRule(self, **kwargs):
        """
        id the ID of the port forwarding rule true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("deletePortForwardingRule", args)

    def createRemoteAccessVpn(self, **kwargs):
        """
        publicipid public ip address id of the vpn server true
        account an optional account for the VPN. Must be used with domainId. false
        domainid an optional domainId for the VPN. If the account parameter is used, domainId must also be used. false
        iprange the range of ip addresses to allocate to vpn clients. The first ip in the range will be taken by the vpn server false
        """
        if not publicipid in kwargs:
            raise RuntimeError("Missing required argument publicipid")
        return self.call("createRemoteAccessVpn", args)

    def enableStaticNat(self, **kwargs):
        """
        ipaddressid the public IP address id for which static nat feature is being enabled true
        virtualmachineid the ID of the virtual machine for enabling static nat feature true
        """
        if not ipaddressid in kwargs:
            raise RuntimeError("Missing required argument ipaddressid")
        if not virtualmachineid in kwargs:
            raise RuntimeError("Missing required argument virtualmachineid")
        return self.call("enableStaticNat", args)

    def listLoadBalancerRules(self, **kwargs):
        """
        account the account of the load balancer rule. Must be used with the domainId parameter. false
        domainid the domain ID of the load balancer rule. If used with the account parameter, lists load balancer rules for the account in the specified domain. false
        id the ID of the load balancer rule false
        name the name of the load balancer rule false
        publicipid the public IP address id of the load balancer rule false
        virtualmachineid the ID of the virtual machine of the load balancer rule false
        """
        return self.call("listLoadBalancerRules", args)

    def addVpnUser(self, **kwargs):
        """
        password password for the username true
        username username for the vpn user true
        account an optional account for the vpn user. Must be used with domainId. false
        domainid an optional domainId for the vpn user. If the account parameter is used, domainId must also be used. false
        """
        if not password in kwargs:
            raise RuntimeError("Missing required argument password")
        if not username in kwargs:
            raise RuntimeError("Missing required argument username")
        return self.call("addVpnUser", args)

    def updateLoadBalancerRule(self, **kwargs):
        """
        id the id of the load balancer rule to update true
        algorithm load balancer algorithm (source, roundrobin, leastconn) false
        description the description of the load balancer rule false
        name the name of the load balancer rule false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("updateLoadBalancerRule", args)

    def deployVirtualMachine(self, **kwargs):
        """
        serviceofferingid the ID of the service offering for the virtual machine true
        templateid the ID of the template for the virtual machine true
        zoneid availability zone for the virtual machine true
        account an optional account for the virtual machine. Must be used with domainId. false
        diskofferingid the ID of the disk offering for the virtual machine. If the template is of ISO format, the diskOfferingId is for the root disk volume. Otherwise this parameter is used to indicate the offering for the data disk volume. If the templateId parameter passed is from a Template object, the diskOfferingId refers to a DATA Disk Volume created. If the templateId parameter passed is from an ISO object, the diskOfferingId refers to a ROOT Disk Volume created. false
        displayname an optional user generated name for the virtual machine false
        domainid an optional domainId for the virtual machine. If the account parameter is used, domainId must also be used. false
        group an optional group for the virtual machine false
        hypervisor the hypervisor on which to deploy the virtual machine false
        keypair name of the ssh key pair used to login to the virtual machine false
        name host name for the virtual machine false
        networkids list of network ids used by virtual machine false
        securitygroupids comma separated list of security groups id that going to be applied to the virtual machine. Should be passed only when vm is created from a zone with Basic Network support false
        size the arbitrary size for the DATADISK volume. Mutually exclusive with diskOfferingId false
        userdata an optional binary data that can be sent to the virtual machine upon a successful deployment. This binary data must be base64 encoded before adding it to the request. Currently only HTTP GET is supported. Using HTTP GET (via querystring), you can send up to 2KB of data after base64 encoding. false
        """
        if not serviceofferingid in kwargs:
            raise RuntimeError("Missing required argument serviceofferingid")
        if not templateid in kwargs:
            raise RuntimeError("Missing required argument templateid")
        if not zoneid in kwargs:
            raise RuntimeError("Missing required argument zoneid")
        return self.call("deployVirtualMachine", args)

    def updateTemplate(self, **kwargs):
        """
        id the ID of the image file true
        bootable true if image is bootable, false otherwise false
        displaytext the display text of the image false
        format the format for the image false
        name the name of the image file false
        ostypeid the ID of the OS type that best represents the OS of this image. false
        passwordenabled true if the image supports the password reset feature; default is false false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("updateTemplate", args)

    def createIpForwardingRule(self, **kwargs):
        """
        ipaddressid the public IP address id of the forwarding rule, already associated via associateIp true
        protocol the protocol for the rule. Valid values are TCP or UDP. true
        startport the start port for the rule true
        endport the end port for the rule false
        """
        if not ipaddressid in kwargs:
            raise RuntimeError("Missing required argument ipaddressid")
        if not protocol in kwargs:
            raise RuntimeError("Missing required argument protocol")
        if not startport in kwargs:
            raise RuntimeError("Missing required argument startport")
        return self.call("createIpForwardingRule", args)

    def revokeSecurityGroupIngress(self, **kwargs):
        """
        id The ID of the ingress rule true
        account an optional account for the security group. Must be used with domainId. false
        domainid an optional domainId for the security group. If the account parameter is used, domainId must also be used. false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("revokeSecurityGroupIngress", args)

    def listEvents(self, **kwargs):
        """
        account the account for the event. Must be used with the domainId parameter. false
        domainid the domain ID for the event. If used with the account parameter, returns all events for an account in the specified domain ID. false
        duration the duration of the event false
        enddate the end date range of the list you want to retrieve (use format "yyyy-MM-dd") false
        entrytime the time the event was entered false
        id the ID of the event false
        level the event level (INFO, WARN, ERROR) false
        startdate the start date range of the list you want to retrieve (use format "yyyy-MM-dd") false
        type the event type (see event types) false
        """
        return self.call("listEvents", args)

    def listHypervisors(self, **kwargs):
        """
        zoneid the zone id for listing hypervisors. false
        """
        return self.call("listHypervisors", args)

    def listServiceOfferings(self, **kwargs):
        """
        domainid the ID of the domain associated with the service offering false
        id ID of the service offering false
        name name of the service offering false
        virtualmachineid the ID of the virtual machine. Pass this in if you want to see the available service offering that a virtual machine can be changed to. false
        """
        return self.call("listServiceOfferings", args)

    def getVMPassword(self, **kwargs):
        """
        id The ID of the virtual machine true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("getVMPassword", args)

    def rebootVirtualMachine(self, **kwargs):
        """
        id The ID of the virtual machine true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("rebootVirtualMachine", args)

    def updateIsoPermissions(self, **kwargs):
        """
        id the template ID true
        accounts a comma delimited list of accounts false
        isfeatured true for featured templates/isos, false otherwise false
        ispublic true for public templates/isos, false for private templates/isos false
        op permission operator (add, remove, reset) false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("updateIsoPermissions", args)

    def listOsCategories(self, **kwargs):
        """
        id list Os category by id false
        """
        return self.call("listOsCategories", args)

    def listNetworkOfferings(self, **kwargs):
        """
        availability the availability of network offering. Default value is Required false
        displaytext list network offerings by display text false
        guestiptype the guest ip type for the network offering, supported types are Direct and Virtual. false
        id list network offerings by id false
        isdefault true if need to list only default network offerings. Default value is false false
        isshared true is network offering supports vlans false
        name list network offerings by name false
        specifyvlan the tags for the network offering. false
        traffictype list by traffic type false
        """
        return self.call("listNetworkOfferings", args)

    def listAsyncJobs(self, **kwargs):
        """
        account the account associated with the async job. Must be used with the domainId parameter. false
        domainid the domain ID associated with the async job.  If used with the account parameter, returns async jobs for the account in the specified domain. false
        startdate the start date of the async job false
        """
        return self.call("listAsyncJobs", args)

    def removeVpnUser(self, **kwargs):
        """
        username username for the vpn user true
        account an optional account for the vpn user. Must be used with domainId. false
        domainid an optional domainId for the vpn user. If the account parameter is used, domainId must also be used. false
        """
        if not username in kwargs:
            raise RuntimeError("Missing required argument username")
        return self.call("removeVpnUser", args)

    def copyTemplate(self, **kwargs):
        """
        id Template ID. true
        destzoneid ID of the zone the template is being copied to. true
        sourcezoneid ID of the zone the template is currently hosted on. true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        if not destzoneid in kwargs:
            raise RuntimeError("Missing required argument destzoneid")
        if not sourcezoneid in kwargs:
            raise RuntimeError("Missing required argument sourcezoneid")
        return self.call("copyTemplate", args)

    def listSnapshotPolicies(self, **kwargs):
        """
        volumeid the ID of the disk volume true
        account lists snapshot policies for the specified account. Must be used with domainid parameter. false
        domainid the domain ID. If used with the account parameter, lists snapshot policies for the specified account in this domain. false
        """
        if not volumeid in kwargs:
            raise RuntimeError("Missing required argument volumeid")
        return self.call("listSnapshotPolicies", args)

    def updateVirtualMachine(self, **kwargs):
        """
        id The ID of the virtual machine true
        displayname user generated name false
        group group of the virtual machine false
        haenable true if high-availability is enabled for the virtual machine, false otherwise false
        ostypeid the ID of the OS type that best represents this VM. false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("updateVirtualMachine", args)

    def listPublicIpAddresses(self, **kwargs):
        """
        account lists all public IP addresses by account. Must be used with the domainId parameter. false
        allocatedonly limits search results to allocated public IP addresses false
        domainid lists all public IP addresses by domain ID. If used with the account parameter, lists all public IP addresses by account for specified domain. false
        forvirtualnetwork the virtual network for the IP address false
        id lists ip address by id false
        ipaddress lists the specified IP address false
        vlanid lists all public IP addresses by VLAN ID false
        zoneid lists all public IP addresses by Zone ID false
        """
        return self.call("listPublicIpAddresses", args)

    def listVirtualMachines(self, **kwargs):
        """
        account account. Must be used with the domainId parameter. false
        domainid the domain ID. If used with the account parameter, lists virtual machines for the specified account in this domain. false
        forvirtualnetwork list by network type; true if need to list vms using Virtual Network, false otherwise false
        groupid the group ID false
        hostid the host ID false
        hypervisor the target hypervisor for the template false
        id the ID of the virtual machine false
        isrecursive defaults to false, but if true, lists all vms from the parent specified by the domain id till leaves. false
        name name of the virtual machine false
        networkid list by network id false
        podid the pod ID false
        state state of the virtual machine false
        zoneid the availability zone ID false
        """
        return self.call("listVirtualMachines", kwargs)

    def registerIso(self, **kwargs):
        """
        displaytext the display text of the ISO. This is usually used for display purposes. true
        name the name of the ISO true
        url the URL to where the ISO is currently being hosted true
        zoneid the ID of the zone you wish to register the ISO to. true
        account an optional account name. Must be used with domainId. false
        bootable true if this ISO is bootable false
        domainid an optional domainId. If the account parameter is used, domainId must also be used. false
        isfeatured true if you want this ISO to be featured false
        ispublic true if you want to register the ISO to be publicly available to all users, false otherwise. false
        ostypeid the ID of the OS Type that best represents the OS of this ISO false
        """
        if not displaytext in kwargs:
            raise RuntimeError("Missing required argument displaytext")
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        if not url in kwargs:
            raise RuntimeError("Missing required argument url")
        if not zoneid in kwargs:
            raise RuntimeError("Missing required argument zoneid")
        return self.call("registerIso", args)

    def listSSHKeyPairs(self, **kwargs):
        """
        fingerprint A public key fingerprint to look for false
        keyword List by keyword false
        name A key pair name to look for false
        page  false
        pagesize  false
        """
        return self.call("listSSHKeyPairs", args)

    def stopVirtualMachine(self, **kwargs):
        """
        id The ID of the virtual machine true
        forced Force stop the VM.  The caller knows the VM is stopped. false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("stopVirtualMachine", args)

    def listIsoPermissions(self, **kwargs):
        """
        id the template ID true
        account List template visibility and permissions for the specified account. Must be used with the domainId parameter. false
        domainid List template visibility and permissions by domain. If used with the account parameter, specifies in which domain the specified account exists. false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("listIsoPermissions", args)

    def listAccounts(self, **kwargs):
        """
        accounttype list accounts by account type. Valid account types are 1 (admin), 2 (domain-admin), and 0 (user). false
        domainid list all accounts in specified domain. If used with the name parameter, retrieves account information for the account with specified name in specified domain. false
        id list account by account ID false
        iscleanuprequired list accounts by cleanuprequred attribute (values are true or false) false
        isrecursive defaults to false, but if true, lists all accounts from the parent specified by the domain id till leaves. false
        name list account by account name false
        state list accounts by state. Valid states are enabled, disabled, and locked. false
        """
        return self.call("listAccounts", args)

    def listTemplates(self, **kwargs):
        """
        templatefilter possible values are "featured", "self", "self-executable", "executable", and "community".* featured-templates that are featured and are public* self-templates that have been registered/created by the owner* selfexecutable-templates that have been registered/created by the owner that can be used to deploy a new VM* executable-all templates that can be used to deploy a new VM* community-templates that are public. true
        account list template by account. Must be used with the domainId parameter. false
        domainid list all templates in specified domain. If used with the account parameter, lists all templates for an account in the specified domain. false
        hypervisor the hypervisor for which to restrict the search false
        id the template ID false
        name the template name false
        zoneid list templates by zoneId false
        """
        if not 'templatefilter' in kwargs:
            raise RuntimeError("Missing required argument templatefilter")
        return self.call("listTemplates", kwargs)

    def resetPasswordForVirtualMachine(self, **kwargs):
        """
        id The ID of the virtual machine true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("resetPasswordForVirtualMachine", args)

    def listVolumes(self, **kwargs):
        """
        account the account associated with the disk volume. Must be used with the domainId parameter. false
        domainid Lists all disk volumes for the specified domain ID. If used with the account parameter, returns all disk volumes for an account in the specified domain ID. false
        hostid list volumes on specified host false
        id the ID of the disk volume false
        isrecursive defaults to false, but if true, lists all volumes from the parent specified by the domain id till leaves. false
        name the name of the disk volume false
        podid the pod id the disk volume belongs to false
        type the type of disk volume false
        virtualmachineid the ID of the virtual machine false
        zoneid the ID of the availability zone false
        """
        return self.call("listVolumes", args)

    def queryAsyncJobResult(self, **kwargs):
        """
        jobid the ID of the asychronous job true
        """
        if not jobid in kwargs:
            raise RuntimeError("Missing required argument jobid")
        return self.call("queryAsyncJobResult", args)

    def detachVolume(self, **kwargs):
        """
        deviceid the device ID on the virtual machine where volume is detached from false
        id the ID of the disk volume false
        virtualmachineid the ID of the virtual machine where the volume is detached from false
        """
        return self.call("detachVolume", args)

    def destroyVirtualMachine(self, **kwargs):
        """
        id The ID of the virtual machine true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("destroyVirtualMachine", args)

    def extractTemplate(self, **kwargs):
        """
        id the ID of the template true
        mode the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD true
        zoneid the ID of the zone where the ISO is originally located true
        url the url to which the ISO would be extracted false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        if not mode in kwargs:
            raise RuntimeError("Missing required argument mode")
        if not zoneid in kwargs:
            raise RuntimeError("Missing required argument zoneid")
        return self.call("extractTemplate", args)

    def attachIso(self, **kwargs):
        """
        id the ID of the ISO file true
        virtualmachineid the ID of the virtual machine true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        if not virtualmachineid in kwargs:
            raise RuntimeError("Missing required argument virtualmachineid")
        return self.call("attachIso", args)

    def updateIso(self, **kwargs):
        """
        id the ID of the image file true
        bootable true if image is bootable, false otherwise false
        displaytext the display text of the image false
        format the format for the image false
        name the name of the image file false
        ostypeid the ID of the OS type that best represents the OS of this image. false
        passwordenabled true if the image supports the password reset feature; default is false false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("updateIso", args)

    def listIpForwardingRules(self, **kwargs):
        """
        account the account associated with the ip forwarding rule. Must be used with the domainId parameter. false
        domainid Lists all rules for this id. If used with the account parameter, returns all rules for an account in the specified domain ID. false
        id Lists rule with the specified ID. false
        ipaddressid list the rule belonging to this public ip address false
        virtualmachineid Lists all rules applied to the specified Vm. false
        """
        return self.call("listIpForwardingRules", args)

    def deleteSnapshotPolicies(self, **kwargs):
        """
        id the Id of the snapshot false
        ids list of snapshots IDs separated by comma false
        """
        return self.call("deleteSnapshotPolicies", args)

    def logout(self, **kwargs):
        """
        """
        return self.call("logout", args)

    def listRemoteAccessVpns(self, **kwargs):
        """
        publicipid public ip address id of the vpn server true
        account the account of the remote access vpn. Must be used with the domainId parameter. false
        domainid the domain ID of the remote access vpn rule. If used with the account parameter, lists remote access vpns for the account in the specified domain. false
        """
        if not publicipid in kwargs:
            raise RuntimeError("Missing required argument publicipid")
        return self.call("listRemoteAccessVpns", args)

    def authorizeSecurityGroupIngress(self, **kwargs):
        """
        securitygroupid The ID of the security group true
        account an optional account for the security group. Must be used with domainId. false
        cidrlist the cidr list associated false
        domainid an optional domainId for the security group. If the account parameter is used, domainId must also be used. false
        endport end port for this ingress rule false
        icmpcode error code for this icmp message false
        icmptype type of the icmp message being sent false
        protocol TCP is default. UDP is the other supported protocol false
        startport start port for this ingress rule false
        usersecuritygrouplist user to security group mapping false
        """
        if not securitygroupid in kwargs:
            raise RuntimeError("Missing required argument securitygroupid")
        return self.call("authorizeSecurityGroupIngress", args)

    def createSnapshot(self, **kwargs):
        """
        volumeid The ID of the disk volume true
        account The account of the snapshot. The account parameter must be used with the domainId parameter. false
        domainid The domain ID of the snapshot. If used with the account parameter, specifies a domain for the account associated with the disk volume. false
        policyid policy id of the snapshot, if this is null, then use MANUAL_POLICY. false
        """
        if not volumeid in kwargs:
            raise RuntimeError("Missing required argument volumeid")
        return self.call("createSnapshot", args)

    def assignToLoadBalancerRule(self, **kwargs):
        """
        id the ID of the load balancer rule true
        virtualmachineids the list of IDs of the virtual machine that are being assigned to the load balancer rule(i.e. virtualMachineIds=1,2,3) true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        if not virtualmachineids in kwargs:
            raise RuntimeError("Missing required argument virtualmachineids")
        return self.call("assignToLoadBalancerRule", args)

    def changeServiceForVirtualMachine(self, **kwargs):
        """
        id The ID of the virtual machine true
        serviceofferingid the service offering ID to apply to the virtual machine true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        if not serviceofferingid in kwargs:
            raise RuntimeError("Missing required argument serviceofferingid")
        return self.call("changeServiceForVirtualMachine", args)

    def deleteNetwork(self, **kwargs):
        """
        id the ID of the network true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("deleteNetwork", args)

    def deleteRemoteAccessVpn(self, **kwargs):
        """
        publicipid public ip address id of the vpn server true
        """
        if not publicipid in kwargs:
            raise RuntimeError("Missing required argument publicipid")
        return self.call("deleteRemoteAccessVpn", args)

    def deleteSnapshot(self, **kwargs):
        """
        id The ID of the snapshot true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("deleteSnapshot", args)

    def deleteIpForwardingRule(self, **kwargs):
        """
        id the id of the forwarding rule true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("deleteIpForwardingRule", args)

    def listCapabilities(self, **kwargs):
        """
        """
        return self.call("listCapabilities", args)

    def listInstanceGroups(self, **kwargs):
        """
        account list instance group belonging to the specified account. Must be used with domainid parameter false
        domainid the domain ID. If used with the account parameter, lists virtual machines for the specified account in this domain. false
        id list instance groups by ID false
        name list instance groups by name false
        """
        return self.call("listInstanceGroups", args)

    def extractVolume(self, **kwargs):
        """
        id the ID of the volume true
        mode the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD true
        zoneid the ID of the zone where the volume is located true
        url the url to which the volume would be extracted false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        if not mode in kwargs:
            raise RuntimeError("Missing required argument mode")
        if not zoneid in kwargs:
            raise RuntimeError("Missing required argument zoneid")
        return self.call("extractVolume", args)

    def updateInstanceGroup(self, **kwargs):
        """
        id Instance group ID true
        name new instance group name false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("updateInstanceGroup", args)

    def attachVolume(self, **kwargs):
        """
        id the ID of the disk volume true
        virtualmachineid the ID of the virtual machine true
        deviceid the ID of the device to map the volume to within the guest OS. If no deviceId is passed in, the next available deviceId will be chosen. Possible values for a Linux OS are:* 1 - /dev/xvdb* 2 - /dev/xvdc* 4 - /dev/xvde* 5 - /dev/xvdf* 6 - /dev/xvdg* 7 - /dev/xvdh* 8 - /dev/xvdi* 9 - /dev/xvdj false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        if not virtualmachineid in kwargs:
            raise RuntimeError("Missing required argument virtualmachineid")
        return self.call("attachVolume", args)

    def listTemplatePermissions(self, **kwargs):
        """
        id the template ID true
        account List template visibility and permissions for the specified account. Must be used with the domainId parameter. false
        domainid List template visibility and permissions by domain. If used with the account parameter, specifies in which domain the specified account exists. false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("listTemplatePermissions", args)

    def createLoadBalancerRule(self, **kwargs):
        """
        algorithm load balancer algorithm (source, roundrobin, leastconn) true
        name name of the load balancer rule true
        privateport the private port of the private ip address/virtual machine where the network traffic will be load balanced to true
        publicipid public ip address id from where the network traffic will be load balanced from true
        publicport the public port from where the network traffic will be load balanced from true
        description the description of the load balancer rule false
        """
        if not algorithm in kwargs:
            raise RuntimeError("Missing required argument algorithm")
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        if not privateport in kwargs:
            raise RuntimeError("Missing required argument privateport")
        if not publicipid in kwargs:
            raise RuntimeError("Missing required argument publicipid")
        if not publicport in kwargs:
            raise RuntimeError("Missing required argument publicport")
        return self.call("createLoadBalancerRule", args)

    def copyIso(self, **kwargs):
        """
        id the ID of the ISO file true
        destzoneid the ID of the destination zone to which the ISO file will be copied true
        sourcezoneid the ID of the source zone from which the ISO file will be copied true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        if not destzoneid in kwargs:
            raise RuntimeError("Missing required argument destzoneid")
        if not sourcezoneid in kwargs:
            raise RuntimeError("Missing required argument sourcezoneid")
        return self.call("copyIso", args)

    def listPortForwardingRules(self, **kwargs):
        """
        account account. Must be used with the domainId parameter. false
        domainid the domain ID. If used with the account parameter, lists port forwarding rules for the specified account in this domain. false
        id Lists rule with the specified ID. false
        ipaddressid the id of IP address of the port forwarding services false
        """
        return self.call("listPortForwardingRules", args)

    def getCloudIdentifier(self, **kwargs):
        """
        userid the user ID for the cloud identifier true
        """
        if not userid in kwargs:
            raise RuntimeError("Missing required argument userid")
        return self.call("getCloudIdentifier", args)

    def deleteIso(self, **kwargs):
        """
        id the ID of the ISO file true
        zoneid the ID of the zone of the ISO file. If not specified, the ISO will be deleted from all the zones false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("deleteIso", args)

    def disableStaticNat(self, **kwargs):
        """
        ipaddressid the public IP address id for which static nat feature is being disableed true
        """
        if not ipaddressid in kwargs:
            raise RuntimeError("Missing required argument ipaddressid")
        return self.call("disableStaticNat", args)

    def detachIso(self, **kwargs):
        """
        virtualmachineid The ID of the virtual machine true
        """
        if not virtualmachineid in kwargs:
            raise RuntimeError("Missing required argument virtualmachineid")
        return self.call("detachIso", args)

    def deleteSecurityGroup(self, **kwargs):
        """
        id The ID of the security group true
        account the account of the security group. Must be specified with domain ID false
        domainid the domain ID of account owning the security group false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("deleteSecurityGroup", args)

    def createVolume(self, **kwargs):
        """
        name the name of the disk volume true
        account the account associated with the disk volume. Must be used with the domainId parameter. false
        diskofferingid the ID of the disk offering. Either diskOfferingId or snapshotId must be passed in. false
        domainid the domain ID associated with the disk offering. If used with the account parameter returns the disk volume associated with the account for the specified domain. false
        size Arbitrary volume size. Mutually exclusive with diskOfferingId false
        snapshotid the snapshot ID for the disk volume. Either diskOfferingId or snapshotId must be passed in. false
        zoneid the ID of the availability zone false
        """
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        return self.call("createVolume", args)

    def createSecurityGroup(self, **kwargs):
        """
        name name of the security group true
        account an optional account for the security group. Must be used with domainId. false
        description the description of the security group false
        domainid an optional domainId for the security group. If the account parameter is used, domainId must also be used. false
        """
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        return self.call("createSecurityGroup", args)

    def listResourceLimits(self, **kwargs):
        """
        account Lists resource limits by account. Must be used with the domainId parameter. false
        domainid Lists resource limits by domain ID. If used with the account parameter, lists resource limits for a specified account in a specified domain. false
        id Lists resource limits by ID. false
        resourcetype Type of resource to update. Values are 0, 1, 2, 3, and 4. 0 - Instance. Number of instances a user can create. 1 - IP. Number of public IP addresses a user can own. 2 - Volume. Number of disk volumes a user can create.3 - Snapshot. Number of snapshots a user can create.4 - Template. Number of templates that a user can register/create. false
        """
        return self.call("listResourceLimits", args)

    def listSnapshots(self, **kwargs):
        """
        account lists snapshot belongig to the specified account. Must be used with the domainId parameter. false
        domainid the domain ID. If used with the account parameter, lists snapshots for the specified account in this domain. false
        id lists snapshot by snapshot ID false
        intervaltype valid values are HOURLY, DAILY, WEEKLY, and MONTHLY. false
        isrecursive defaults to false, but if true, lists all snapshots from the parent specified by the domain id till leaves. false
        name lists snapshot by snapshot name false
        snapshottype valid values are MANUAL or RECURRING. false
        volumeid the ID of the disk volume false
        """
        return self.call("listSnapshots", args)

    def disassociateIpAddress(self, **kwargs):
        """
        id the id of the public ip address to disassociate true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("disassociateIpAddress", args)

    def createInstanceGroup(self, **kwargs):
        """
        name the name of the instance group true
        account the account of the instance group. The account parameter must be used with the domainId parameter. false
        domainid the domain ID of account owning the instance group false
        """
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        return self.call("createInstanceGroup", args)

    def listZones(self, **kwargs):
        """
        available true if you want to retrieve all available Zones. False if you only want to return the Zones from which you have at least one VM. Default is false. false
        domainid the ID of the domain associated with the zone false
        id the ID of the zone false
        """
        return self.call("listZones", args)

    def registerSSHKeyPair(self, **kwargs):
        """
        name Name of the keypair true
        publickey Public key material of the keypair true
        """
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        if not publickey in kwargs:
            raise RuntimeError("Missing required argument publickey")
        return self.call("registerSSHKeyPair", args)

    def deleteVolume(self, **kwargs):
        """
        id The ID of the disk volume true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("deleteVolume", args)

    def listLoadBalancerRuleInstances(self, **kwargs):
        """
        id the ID of the load balancer rule true
        applied true if listing all virtual machines currently applied to the load balancer rule; default is true false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("listLoadBalancerRuleInstances", args)

    def registerTemplate(self, **kwargs):
        """
        displaytext the display text of the template. This is usually used for display purposes. true
        format the format for the template. Possible values include QCOW2, RAW, and VHD. true
        hypervisor the target hypervisor for the template true
        name the name of the template true
        ostypeid the ID of the OS Type that best represents the OS of this template. true
        url the URL of where the template is hosted. Possible URL include http:// and https:// true
        zoneid the ID of the zone the template is to be hosted on true
        account an optional accountName. Must be used with domainId. false
        bits 32 or 64 bits support. 64 by default false
        domainid an optional domainId. If the account parameter is used, domainId must also be used. false
        isextractable true if the template or its derivatives are extractable; default is false false
        isfeatured true if this template is a featured template, false otherwise false
        ispublic true if the template is available to all accounts; default is true false
        passwordenabled true if the template supports the password reset feature; default is false false
        requireshvm true if this template requires HVM false
        """
        if not displaytext in kwargs:
            raise RuntimeError("Missing required argument displaytext")
        if not format in kwargs:
            raise RuntimeError("Missing required argument format")
        if not hypervisor in kwargs:
            raise RuntimeError("Missing required argument hypervisor")
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        if not ostypeid in kwargs:
            raise RuntimeError("Missing required argument ostypeid")
        if not url in kwargs:
            raise RuntimeError("Missing required argument url")
        if not zoneid in kwargs:
            raise RuntimeError("Missing required argument zoneid")
        return self.call("registerTemplate", args)

    def createSSHKeyPair(self, **kwargs):
        """
        name Name of the keypair true
        account an optional account for the ssh key. Must be used with domainId. false
        domainid an optional domainId for the ssh key. If the account parameter is used, domainId must also be used. false
        """
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        return self.call("createSSHKeyPair", args)

    def listDiskOfferings(self, **kwargs):
        """
        domainid the ID of the domain of the disk offering. false
        id ID of the disk offering false
        name name of the disk offering false
        """
        return self.call("listDiskOfferings", args)

    def createPortForwardingRule(self, **kwargs):
        """
        ipaddressid the IP address id of the port forwarding rule true
        privateport the private port of the port forwarding rule true
        protocol the protocol for the port fowarding rule. Valid values are TCP or UDP. true
        publicport the public port of the port forwarding rule true
        virtualmachineid the ID of the virtual machine for the port forwarding rule true
        """
        if not ipaddressid in kwargs:
            raise RuntimeError("Missing required argument ipaddressid")
        if not privateport in kwargs:
            raise RuntimeError("Missing required argument privateport")
        if not protocol in kwargs:
            raise RuntimeError("Missing required argument protocol")
        if not publicport in kwargs:
            raise RuntimeError("Missing required argument publicport")
        if not virtualmachineid in kwargs:
            raise RuntimeError("Missing required argument virtualmachineid")
        return self.call("createPortForwardingRule", args)

    def createTemplate(self, **kwargs):
        """
        displaytext the display text of the template. This is usually used for display purposes. true
        name the name of the template true
        ostypeid the ID of the OS Type that best represents the OS of this template. true
        bits 32 or 64 bit false
        isfeatured true if this template is a featured template, false otherwise false
        ispublic true if this template is a public template, false otherwise false
        passwordenabled true if the template supports the password reset feature; default is false false
        requireshvm true if the template requres HVM, false otherwise false
        snapshotid the ID of the snapshot the template is being created from false
        volumeid the ID of the disk volume the template is being created from false
        """
        if not displaytext in kwargs:
            raise RuntimeError("Missing required argument displaytext")
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        if not ostypeid in kwargs:
            raise RuntimeError("Missing required argument ostypeid")
        return self.call("createTemplate", args)

    def deleteSSHKeyPair(self, **kwargs):
        """
        name Name of the keypair true
        account the account associated with the keypair. Must be used with the domainId parameter. false
        domainid the domain ID associated with the keypair false
        """
        if not name in kwargs:
            raise RuntimeError("Missing required argument name")
        return self.call("deleteSSHKeyPair", args)

    def listOsTypes(self, **kwargs):
        """
        id list by Os type Id false
        oscategoryid list by Os Category id false
        """
        return self.call("listOsTypes", args)

    def updateTemplatePermissions(self, **kwargs):
        """
        id the template ID true
        accounts a comma delimited list of accounts false
        isfeatured true for featured templates/isos, false otherwise false
        ispublic true for public templates/isos, false for private templates/isos false
        op permission operator (add, remove, reset) false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("updateTemplatePermissions", args)

    def extractIso(self, **kwargs):
        """
        id the ID of the ISO file true
        mode the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD true
        zoneid the ID of the zone where the ISO is originally located true
        url the url to which the ISO would be extracted false
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        if not mode in kwargs:
            raise RuntimeError("Missing required argument mode")
        if not zoneid in kwargs:
            raise RuntimeError("Missing required argument zoneid")
        return self.call("extractIso", args)

    def login(self, **kwargs):
        """
        username Username true
        password Password true
        domain path of the domain that the user belongs to. Example: domain=/com/cloud/internal.  If no domain is passed in, the ROOT domain is assumed. false
        """
        if not username in kwargs:
            raise RuntimeError("Missing required argument username")
        if not password in kwargs:
            raise RuntimeError("Missing required argument password")
        return self.call("login", args)

    def listSecurityGroups(self, **kwargs):
        """
        account lists all available port security groups for the account. Must be used with domainID parameter false
        domainid lists all available security groups for the domain ID. If used with the account parameter, lists all available security groups for the account in the specified domain ID. false
        id list the security group by the id provided false
        securitygroupname lists security groups by name false
        virtualmachineid lists security groups by virtual machine id false
        """
        return self.call("listSecurityGroups", args)

    def listNetworks(self, **kwargs):
        """
        account account who will own the VLAN. If VLAN is Zone wide, this parameter should be ommited false
        domainid domain ID of the account owning a VLAN false
        id list networks by id false
        isdefault true if network is default, false otherwise false
        isshared true if network is shared, false otherwise false
        issystem true if network is system, false otherwise false
        traffictype type of the traffic false
        type the type of the network false
        zoneid the Zone ID of the network false
        """
        return self.call("listNetworks", args)

    def deleteInstanceGroup(self, **kwargs):
        """
        id the ID of the instance group true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("deleteInstanceGroup", args)

    def listVpnUsers(self, **kwargs):
        """
        account the account of the remote access vpn. Must be used with the domainId parameter. false
        domainid the domain ID of the remote access vpn. If used with the account parameter, lists remote access vpns for the account in the specified domain. false
        id the ID of the vpn user false
        username the username of the vpn user. false
        """
        return self.call("listVpnUsers", args)

    def createSnapshotPolicy(self, **kwargs):
        """
        intervaltype valid values are HOURLY, DAILY, WEEKLY, and MONTHLY true
        maxsnaps maximum number of snapshots to retain true
        schedule time the snapshot is scheduled to be taken. Format is:* if HOURLY, MM* if DAILY, MM:HH* if WEEKLY, MM:HH:DD (1-7)* if MONTHLY, MM:HH:DD (1-28) true
        timezone Specifies a timezone for this command. For more information on the timezone parameter, see Time Zone Format. true
        volumeid the ID of the disk volume true
        """
        if not intervaltype in kwargs:
            raise RuntimeError("Missing required argument intervaltype")
        if not maxsnaps in kwargs:
            raise RuntimeError("Missing required argument maxsnaps")
        if not schedule in kwargs:
            raise RuntimeError("Missing required argument schedule")
        if not timezone in kwargs:
            raise RuntimeError("Missing required argument timezone")
        if not volumeid in kwargs:
            raise RuntimeError("Missing required argument volumeid")
        return self.call("createSnapshotPolicy", args)

    def deleteLoadBalancerRule(self, **kwargs):
        """
        id the ID of the load balancer rule true
        """
        if not id in kwargs:
            raise RuntimeError("Missing required argument id")
        return self.call("deleteLoadBalancerRule", args)

