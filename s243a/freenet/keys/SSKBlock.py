Based on https://github.com/freenet/fred/blob/4e6bf4b0ea42b713a4261778fac9ca376dc28117/src/freenet/keys/SSKBlock.java#L39

#/* This code is part of Freenet. It is distributed under the GNU General
# * Public License, version 2 (or at your option any later version). See
# * http://www.gnu.org/ for further details of the GPL. */
##package freenet.keys;

##import org.bouncycastle.crypto.params.DSAPublicKeyParameters;
##import org.bouncycastle.crypto.signers.DSASigner;
##import freenet.crypt.DSAPublicKey;

from Crypto.PublicKey import DSA
from Crypto.Signature import DSS

##import freenet.crypt.SHA256;
##import java.security.MessageDigest;

from Crypto.Hash import SHA256
from interface import implements, Interface 

##import freenet.crypt.Global;
##import freenet.support.Fields;
##import freenet.support.HexUtil;
##import freenet.support.Logger;
#
#/**
# * SSKBlock. Contains a full fetched key. Can do a node-level verification. Can 
# * decode original data when fed a ClientSSK.
# */
#public class SSKBlock implements KeyBlock {

#	/* HEADERS FORMAT:
#	 * 2 bytes - hash ID
#	 * 2 bytes - symmetric cipher ID
#	 * 32 bytes - E(H(docname))
#	 * ENCRYPTED WITH E(H(docname)) AS IV:
#	 *  32 bytes - H(decrypted data), = data decryption key
#	 *  2 bytes - data length + metadata flag
#	 *  2 bytes - data compression algorithm or -1
#	 * IMPLICIT - hash of data
#	 * IMPLICIT - hash of remaining fields, including the implicit hash of data
#	 * 
#	 * SIGNATURE ON THE ABOVE HASH:
#	 *  32 bytes - signature: R (unsigned bytes)
#	 *  32 bytes - signature: S (unsigned bytes)
#	 * 
#	 * PLUS THE PUBKEY:
#	 *  Pubkey
#	 *  Group
#	 */

#Need to add import for NodeSSK
from freenet.keys import KeyBlock
class SSKBlock(implements(KeyBlock)):
#	#	public SSKBlock(byte[] data, byte[] headers, NodeSSK nodeKey, boolean dontVerify) throws SSKVerifyException {
    __init__(self,
             data=None, # byte[] or list 
             headers=None, #byte[] or list
             nodeKey=None, #NodeSSK
             dontVerify=False ##boolean i'm guessing that we always want to verify
             **kw
            ) //throws SSKVerifyException {
#	private static volatile boolean logMINOR;
#	
#	static {
#		Logger.registerClass(SSKBlock.class);
#	}
#	
#	// how much of the headers we compare in order to consider two
#	// SSKBlocks equal - necessary because the last 64 bytes need not
#	// be the same for the same data and the same key (see comments below)
#	private static final int HEADER_COMPARE_TO = 71;

# Add option to read values from file here
         if (not dontVerify) and (headers.length != TOTAL_HEADERS_LENGTH):
#			throw new IllegalArgumentException("Headers.length="+headers.length+" should be "+TOTAL_HEADERS_LENGTH);
             #TODO - Implement IllegalArgumentException
             pass
#		this.data = data;


        self.dontVerify=dontVerify   #boolean i'm guessing that we always want to verify
        try:
            this.pubKey = nodeKey.getPubKey();
        except: #Not part of the orginal freenet Java
            self.nodeKey=kw.get('nodeKey',None)
            #Maybe log here that we didn't get the nodeKey from a NodeSSK object.
            #since this might not be a normal case
            #Maybe throw an exception if dontVerify=True
        if (not dontVerify) and pubKey is None:
            #throw new SSKVerifyException("PubKey was null from "+nodeKey);
            #TODO - Implement SSKVerifyException
            pass #Maybe log if dontVerify=True since it might not be the normal case       
        self.data=data               # byte[] or list 
        if (not dontVerify) and (data.length != DATA_LENGTH):
#			throw new SSKVerifyException("Data length wrong: "+data.length+" should be "+DATA_LENGTH);
            #TODO - Implement SSKVerifyException
            #Mabye log here, since this might not be the normal case
            pass #Maybe log if dontVerify=True since it might not be the normal case

        self.headers=selfToHdrLst(headers=headers,data=data,fileName=fileName)#byte[] or list  
#        // Now verify it
#        hashIdentifier = (short)(((headers[0] & 0xff) << 8) + (headers[1] & 0xff));
#        if(hashIdentifier != HASH_SHA256)
#            throw new SSKVerifyException("Hash not SHA-256");
#        int x = 2;
#		symCipherIdentifier = (short)(((headers[x] & 0xff) << 8) + (headers[x+1] & 0xff));
#		x+=2;
#		// Then E(H(docname))
#		byte[] ehDocname = new byte[E_H_DOCNAME_LENGTH];

#		System.arraycopy(headers, x, ehDocname, 0, ehDocname.length);
#		x += E_H_DOCNAME_LENGTH;
#		headersOffset = x; // is index to start of encrypted headers
#		x += ENCRYPTED_HEADERS_LENGTH;
#		// Extract the signature
#		if(x+SIG_R_LENGTH+SIG_S_LENGTH > headers.length)
#			throw new SSKVerifyException("Headers too short: "+headers.length+" should be at least "+x+SIG_R_LENGTH+SIG_S_LENGTH);
#		// Compute the hash on the data


#	/** The index of the first byte of encrypted fields in the headers, after E(H(docname)) */
        self.headersOffset=0 ## is index to start of encrypted headers (set later)

        self.pupKey=kw.get('pupKey',None) #DSAPublicKey
        self.hashIdentifier('hashIdentifier',None) #short
        self.symCipherIdentifier('symCipherIdentifier',None) #short 
        self.hCode('hashCode',None) #short, in python the property and method can't hava the same name so the property name was shortened
        self.DATA_LENGTH = 1024 #short    
#    /* Maximum length of compressed payload */
        self.MAX_COMPRESSED_DATA_LENGTH = DATA_LENGTH - 2 #init    
        self.SIG_R_LENGTH = 32 #short
        self.SIG_S_LENGTH = 32 #short
        self.E_H_DOCNAME_LENGTH = 32 #short
        self.TOTAL_HEADERS_LENGTH = 2 + SIG_R_LENGTH + SIG_S_LENGTH + 2 + 
                                    E_H_DOCNAME_LENGTH + 
                                    ClientSSKBlock.DATA_DECRYPT_KEY_LENGTH + 
                                    2 + 2 # #short
        self.ENCRYPTED_HEADERS_LENGTH = 36 #short
    
#    @Override
    def equals(self,o): #returns boolean
        if not isinstance(o, SSKBlock):
            return False
#    	SSKBlock block = (SSKBlock)o; #I don't think anything like casting is necessary in python here
        block = o #Just to keep the symantics like the Java, not really necessary
#    	if(!block.pubKey.equals(pubKey)) return false;
        if not block.pubKey.equals(pupKey):
            return False
        if not block.nodeKey.equals(nodeKey):
            return False
        if block.headersOffset != headersOffset:
            return False
        if block.hashIdentifier != hashIdentifier:
            return False
        if block.symCipherIdentifier != symCipherIdentifier:
            return False
        #// only compare some of the headers (see top)
        for i in Range(0,HEADER_COMPARE_TO-1):
            if block.headers[i] != headers[i]):
                return false;
# We may want to write a custom equality function here that considers more conditions                
        if block.data == data #Was in java: not Arrays.equals(block.data, data))
             return false;
        return true;
#    @Override
    def hashCode() #returns int
        return hCode;

#		if(!dontVerify || logMINOR) {	// force verify on log minor
#			byte[] bufR = new byte[SIG_R_LENGTH];
#			byte[] bufS = new byte[SIG_S_LENGTH];
#			
#			System.arraycopy(headers, x, bufR, 0, SIG_R_LENGTH);
#			x+=SIG_R_LENGTH;
#			System.arraycopy(headers, x, bufS, 0, SIG_S_LENGTH);
#			x+=SIG_S_LENGTH;
#
#			MessageDigest md = null;
#			byte[] overallHash;
#			try {
#				md = SHA256.getMessageDigest();
#				md.update(data);
#				byte[] dataHash = md.digest();
#				// All headers up to and not including the signature
#				md.update(headers, 0, headersOffset + ENCRYPTED_HEADERS_LENGTH);
#				// Then the implicit data hash
#				md.update(dataHash);
#				// Makes the implicit overall hash
#				overallHash = md.digest();
#			} finally {
#				SHA256.returnMessageDigest(md);
#			}
#			
#			// Now verify it
#			BigInteger r = new BigInteger(1, bufR);
#			BigInteger s = new BigInteger(1, bufS);
#			DSASigner dsa = new DSASigner();
#			dsa.init(false, new DSAPublicKeyParameters(pubKey.getY(), Global.getDSAgroupBigAParameters()));
#
#			// We probably don't need to try both here...
#			// but that's what the legacy code was doing...
#			// @see comments in Global before touching it
#			if(!(dsa.verifySignature(Global.truncateHash(overallHash), r, s) ||
#			     dsa.verifySignature(overallHash, r, s))
#			  ) {
#				if (dontVerify)
#					Logger.error(this, "DSA verification failed with dontVerify!!!!");
#				throw new SSKVerifyException("Signature verification failed for node-level SSK");
#			}
#		} // x isn't verified otherwise so no need to += SIG_R_LENGTH + SIG_S_LENGTH
#		if(!Arrays.equals(ehDocname, nodeKey.encryptedHashedDocname))
#			throw new SSKVerifyException("E(H(docname)) wrong - wrong key?? \nfrom headers: "+HexUtil.bytesToHex(ehDocname)+"\nfrom key:     "+HexUtil.bytesToHex(nodeKey.encryptedHashedDocname));
#		hashCode = Fields.hashCode(data) ^ Fields.hashCode(headers) ^ nodeKey.hashCode() ^ pubKey.hashCode() ^ hashIdentifier;
#	}
#
#	@Override
#	public NodeSSK getKey() {
#		return nodeKey;
#	}
#
#	@Override
#	public byte[] getRawHeaders() {
#		return headers;
#	}
#
#	@Override
#	public byte[] getRawData() {
#		return data;
#	}
##
#	public DSAPublicKey getPubKey() {
#		return pubKey;
#	}
#
#	@Override
#	public byte[] getPubkeyBytes() {
#		return pubKey.asBytes();
#	}
#
#	@Override
#	public byte[] getFullKey() {
#		return getKey().getFullKey();
#	}
#
#	@Override
#	public byte[] getRoutingKey() {
#		return getKey().getRoutingKey();
#	}
#	
#}
